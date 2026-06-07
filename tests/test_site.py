# -*- coding: utf-8 -*-
"""
Suíte de testes do portfólio (Python puro — biblioteca padrão, sem dependências).

Como rodar (a partir da pasta do projeto):
    python -m unittest discover -s tests -v
ou:
    python tests/test_site.py

O que é verificado:
  - Arquivos essenciais existem (páginas, CSS, JS, favicon, imagem social...)
  - Estrutura de cada página (DOCTYPE, lang, um único <h1>, <title>, meta description)
  - Toda página referencia o CSS e o JS
  - Navegação e rodapé presentes e consistentes nas 8 páginas
  - Acessibilidade básica (skip-link, landmark #conteudo)
  - SEO/social (og:title, og:description, og:image, twitter:card, favicon)
  - RESTRIÇÃO DE MARCA: nenhuma página pode conter "acriflex"
  - Integridade de links internos (.html apontam para arquivos existentes)
  - Integridade de assets (assets/... existem)
  - Sem links absolutos de raiz (href="/...") que quebram em subpasta do GitHub Pages
  - Dados de contato corretos (WhatsApp, e-mail, LinkedIn, GitHub)
"""
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONTENT_PAGES = [
    "index.html", "sistema.html", "cases.html",
    "case-sistema-industrial.html", "case-churn.html", "case-meritocracia.html",
    "competencias.html", "contato.html",
]
NAV_LINKS = ["index.html", "sistema.html", "cases.html", "competencias.html", "contato.html"]
REQUIRED_FILES = CONTENT_PAGES + [
    "404.html", "robots.txt", "favicon.svg", "README.md",
    "assets/styles.css", "assets/main.js", "assets/img/og-cover.png",
]


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def hrefs(html):
    return re.findall(r'(?:href|src)="([^"]+)"', html)


class TestRequiredFiles(unittest.TestCase):
    def test_required_files_exist(self):
        for rel in REQUIRED_FILES:
            with self.subTest(arquivo=rel):
                self.assertTrue(os.path.exists(os.path.join(ROOT, rel)),
                                "Arquivo essencial faltando: %s" % rel)


class TestPageStructure(unittest.TestCase):
    def test_doctype_and_lang(self):
        for p in CONTENT_PAGES:
            html = read(p)
            with self.subTest(pagina=p):
                self.assertTrue(html.lstrip().lower().startswith("<!doctype html>"), "Sem DOCTYPE: %s" % p)
                self.assertIn('lang="pt-BR"', html, "Sem lang pt-BR: %s" % p)

    def test_single_h1(self):
        for p in CONTENT_PAGES:
            n = len(re.findall(r"<h1[\s>]", read(p)))
            with self.subTest(pagina=p):
                self.assertEqual(n, 1, "Esperado exatamente 1 <h1> em %s, achei %d" % (p, n))

    def test_title_and_description(self):
        for p in CONTENT_PAGES:
            html = read(p)
            title = re.search(r"<title>(.*?)</title>", html, re.S)
            desc = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
            with self.subTest(pagina=p):
                self.assertTrue(title and title.group(1).strip(), "Título vazio: %s" % p)
                self.assertTrue(desc and len(desc.group(1).strip()) > 20, "Meta description fraca/ausente: %s" % p)

    def test_references_css_and_js(self):
        for p in CONTENT_PAGES:
            html = read(p)
            with self.subTest(pagina=p):
                self.assertIn('assets/styles.css', html, "Não referencia o CSS: %s" % p)
                self.assertIn('assets/main.js', html, "Não referencia o JS: %s" % p)


class TestNavAndFooter(unittest.TestCase):
    def test_nav_links_present(self):
        for p in CONTENT_PAGES:
            html = read(p)
            for link in NAV_LINKS:
                with self.subTest(pagina=p, link=link):
                    self.assertIn('href="%s"' % link, html, "Link de nav '%s' ausente em %s" % (link, p))

    def test_footer_present(self):
        for p in CONTENT_PAGES:
            with self.subTest(pagina=p):
                self.assertIn("<footer", read(p), "Rodapé ausente: %s" % p)


class TestAccessibility(unittest.TestCase):
    def test_skip_link_and_landmark(self):
        for p in CONTENT_PAGES:
            html = read(p)
            with self.subTest(pagina=p):
                self.assertIn('class="skip-link"', html, "Skip-link ausente: %s" % p)
                self.assertIn('id="conteudo"', html, "Landmark #conteudo ausente: %s" % p)

    def test_menu_toggle_has_aria(self):
        for p in CONTENT_PAGES:
            html = read(p)
            with self.subTest(pagina=p):
                self.assertIn('aria-expanded', html, "menu-toggle sem aria-expanded: %s" % p)


class TestSeoSocial(unittest.TestCase):
    def test_open_graph_and_twitter(self):
        for p in CONTENT_PAGES:
            html = read(p)
            for needle in ['property="og:title"', 'property="og:description"',
                           'property="og:image"', 'name="twitter:card"']:
                with self.subTest(pagina=p, meta=needle):
                    self.assertIn(needle, html, "%s ausente em %s" % (needle, p))

    def test_favicon(self):
        for p in CONTENT_PAGES:
            with self.subTest(pagina=p):
                self.assertIn('rel="icon"', read(p), "Favicon ausente: %s" % p)


class TestBrandConstraint(unittest.TestCase):
    """Restrição rígida: a marca da empresa NÃO pode aparecer no site."""
    def test_no_acriflex_anywhere(self):
        for p in CONTENT_PAGES + ["404.html", "README.md", "assets/styles.css", "assets/main.js"]:
            with self.subTest(arquivo=p):
                self.assertNotIn("acriflex", read(p).lower(), "Marca proibida encontrada em %s" % p)


class TestLinkIntegrity(unittest.TestCase):
    def test_internal_html_links_resolve(self):
        for p in CONTENT_PAGES + ["404.html"]:
            for h in hrefs(read(p)):
                target = h.split("#")[0]
                if target.endswith(".html") and not target.startswith("http"):
                    with self.subTest(pagina=p, link=h):
                        self.assertTrue(os.path.exists(os.path.join(ROOT, target)),
                                        "Link interno quebrado em %s -> %s" % (p, h))

    def test_assets_resolve(self):
        for p in CONTENT_PAGES + ["404.html"]:
            for h in hrefs(read(p)):
                if h.startswith("assets/"):
                    with self.subTest(pagina=p, asset=h):
                        self.assertTrue(os.path.exists(os.path.join(ROOT, h.split("#")[0])),
                                        "Asset quebrado em %s -> %s" % (p, h))

    def test_no_root_absolute_links(self):
        # href="/..." quebra quando o site é servido em subpasta (GitHub Pages project page)
        for p in CONTENT_PAGES:
            for h in hrefs(read(p)):
                with self.subTest(pagina=p, link=h):
                    self.assertFalse(h.startswith("/"), "Link absoluto de raiz (quebra em subpasta) em %s -> %s" % (p, h))


class TestContactInfo(unittest.TestCase):
    def test_contact_details(self):
        html = read("contato.html") + read("index.html")
        checks = {
            "WhatsApp": "5551981687088",
            "E-mail": "douglastassinarii@gmail.com",
            "LinkedIn": "douglastassinari",
            "GitHub": "DouglasTassinari",
        }
        for nome, valor in checks.items():
            with self.subTest(contato=nome):
                self.assertIn(valor, html, "Contato %s ('%s') ausente." % (nome, valor))


class TestAssetsContent(unittest.TestCase):
    def test_css_has_tokens(self):
        css = read("assets/styles.css")
        for token in ["--accent", "--bg", ".reveal", ".skip-link"]:
            with self.subTest(token=token):
                self.assertIn(token, css, "Token/regra ausente no CSS: %s" % token)

    def test_js_robustness(self):
        js = read("assets/main.js")
        self.assertIn("IntersectionObserver", js)
        self.assertIn("__revealFailsafe", js)


if __name__ == "__main__":
    unittest.main(verbosity=2)

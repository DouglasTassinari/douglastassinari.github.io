# Portfólio · Douglas Tassinari — Arquiteto de Sistemas de Gestão

Site profissional (multi-página, estático) que posiciona o Douglas como **construtor de sistemas corporativos de gestão**, não como criador de dashboards.

> Conceito central: *"Transformo operações em sistemas inteligentes de gestão."*

---

## 📁 Estrutura dos arquivos

```
portfolio/
├── index.html                      → Início (Home)
├── sistema.html                    → O Sistema (a página mais importante)
├── cases.html                      → Índice de cases
├── case-sistema-industrial.html    → Case 01 (sistema-referência)
├── case-churn.html                 → Case 02 (Comercial)
├── case-meritocracia.html          → Case 03 (Pessoas & Indicadores)
├── competencias.html               → Competências
├── contato.html                    → Contato
├── 404.html                        → Página de erro (mesma identidade)
├── favicon.svg                     → Ícone da aba do navegador
├── robots.txt                      → Indexação por buscadores
├── assets/
│   ├── styles.css                  → Design system (todo o visual)
│   ├── main.js                     → Menu mobile, estado ativo, animações
│   └── img/
│       └── og-cover.png            → Imagem de compartilhamento (LinkedIn/WhatsApp)
├── tests/
│   └── test_site.py                → Testes automatizados (link/estrutura/marca)
└── README.md
```

Tudo é **HTML + CSS + JS puro** — sem dependências, sem build. O visual (grade, brilhos, diagrama) é feito em CSS, então o site **não depende de imagem** para ficar bonito.

---

## 👀 Ver no seu computador

**Opção simples:** dê dois cliques em `index.html` — abre direto no navegador.

**Opção recomendada** (links e fontes funcionam melhor com um servidor local):
```powershell
cd "C:\Users\anali\Desktop\portfolio"
python -m http.server 8000
```
Depois abra <http://localhost:8000> no navegador.

---

## 🚀 Publicar no GitHub Pages

1. Crie um repositório no GitHub (ex.: `portfolio` ou `douglastassinari.github.io`).
2. Envie **todo o conteúdo desta pasta** para o repositório (os `.html` na raiz).
3. No GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**.
4. Escolha a branch `main` e a pasta `/ (root)` → **Save**.
5. Em ~1 minuto o site fica no ar em `https://SEU-USUARIO.github.io/portfolio/`.

> Dica: se publicar como `SEU-USUARIO.github.io` (repositório com esse nome exato), o endereço fica sem o `/portfolio` no final.

---

## 🖼️ O que você precisa adicionar

O site funciona sem nada disso, mas estes itens deixam tudo completo:

| Arquivo | Onde colocar | Para quê |
|---|---|---|
| `curriculo.pdf` | na **raiz** da pasta | botão "Baixar currículo" na página Contato |
| imagens (foto, etc.) | em `assets/img/` | se quiser usar depois |
| `favicon` | raiz (ex.: `favicon.svg`) | ícone na aba do navegador (opcional) |

> O botão de currículo aponta para `curriculo.pdf`. Renomeie o seu PDF para esse nome (ou me avise para eu trocar o link).

---

## ✏️ Onde editar o conteúdo

- **Textos:** direto em cada `.html` — o conteúdo está em português, com comentários `<!-- -->` indicando cada seção.
- **Cores e fontes:** em `assets/styles.css`, bloco `:root` (lá no topo) — muda tudo de uma vez.
- **Links de contato (WhatsApp, LinkedIn, e-mail, GitHub):** aparecem no rodapé de todas as páginas e na página `contato.html`.

---

## ✅ Testes automatizados

Tem uma suíte de testes (Python puro, sem instalar nada) que garante que o site não quebre — verifica links, estrutura, acessibilidade, SEO e a regra de **não usar a marca da empresa**. Rode a partir da pasta do projeto:

```powershell
python -m unittest discover -s tests -v
```

Se tudo estiver certo, termina com **OK**. Rode isso sempre que mexer no site.

---

## 🔁 Quando publicar no domínio final

Hoje a imagem de compartilhamento social (`og:image`) aponta para a URL atual de testes (`.../DouglasTassinariv2.github.io/...`). Quando você mover o site para o domínio definitivo, é só me avisar que eu atualizo esse endereço em um lugar só — ou troque você mesmo o valor de `og:image` no `<head>` das páginas.

---

## 🎨 Identidade visual

Paleta e tipografia **próprias** (azul-azure `#4F8DF5` + índigo `#7C5CFF` sobre fundo quase-preto; fontes Space Grotesk + Inter + JetBrains Mono). Inspirada num DNA corporativo/industrial premium, porém **100% autoral** — sem usar logo, nome ou símbolos de qualquer empresa.

---

© 2026 Douglas Tassinari da Silva · Business Systems & Analytics · Criciúma, SC

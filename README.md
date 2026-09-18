# douglastassinari.github.io

Site profissional de Douglas Tassinari — **Sistemas de Gestão & Dados**.

Não é um portfólio de inventário: é um argumento com prova. A home apresenta a
tese ("transformo operações em sistemas de gestão") com três números de impacto,
o que essa experiência leva para outra operação e o trabalho selecionado — um
case a fundo e três projetos que mostram o mesmo raciocínio em outros contextos:

| Página | Natureza | Prova |
|---|---|---|
| [Plataforma Industrial](https://douglastassinari.github.io/cases/plataforma-industrial/) | Case principal | Números de antes e depois conferidos no sistema, descritos sem dados sensíveis |
| [Jornada Brasil](https://douglastassinari.github.io/cases/jornada-brasil/) | Produto público | [jornadabrasil.com.br](https://jornadabrasil.com.br) — no ar |
| [Recomendação de imóveis](https://douglastassinari.github.io/cases/recomendacao-imoveis/) | Cliente externo | Em uso desde jun/2026 — confidencial, sem nome e sem telas |
| [Sistema TAZZIN](https://douglastassinari.github.io/cases/tazzin/) | Código aberto | [Demo no ar](https://tazzin.streamlit.app) · [código no GitHub](https://github.com/DouglasTassinari/Tazzin) |

## Estrutura

```
/
├── index.html                      # Home: hero, impacto, cases, método, trajetória, stack, contato
├── cases/
│   ├── plataforma-industrial/      # Case principal · indústria
│   ├── jornada-brasil/             # Projeto · produto público
│   ├── recomendacao-imoveis/       # Projeto · cliente externo
│   ├── tazzin/                     # Projeto · código aberto
│   └── opsvision/                  # redirect do nome antigo → /cases/tazzin/
├── assets/
│   ├── css/style.css               # Folha única — design system com tokens em :root
│   ├── js/main.js                  # Menu mobile + animação (progressive enhancement)
│   └── img/                        # Foto e imagem Open Graph
├── 404.html
├── sitemap.xml
└── robots.txt
```

## Decisões

- **HTML estático puro, sem build step** — o site é o artefato; qualquer avaliador
  pode ler o fonte no navegador. Deploy é um push (GitHub Pages).
- **Uma folha de CSS para todas as páginas** — tokens em `:root`, sem duplicação.
- **Um padrão único de case, impacto primeiro** — título que é o resultado, resumo
  em 30 segundos (desafio, o que fiz, resultado, papel), antes e depois, evolução,
  duas ou três decisões com a alternativa rejeitada e aprendizados. A profundidade
  técnica fica num bloco recolhido (`<details>`), para quem quiser abrir.
- **Números com fonte** — cada número de impacto foi conferido no sistema de origem
  ou vem de relato do autor com a fonte indicada; o que não se confirmou saiu.
- **Diagramas de arquitetura em HTML/CSS** — sem imagem para carregar, legíveis
  por leitor de tela (`role="img"` + `aria-label`), consistentes com o tema.
- **JavaScript como aprimoramento, não dependência** — sem JS o site permanece
  completo e navegável; `prefers-reduced-motion` é respeitado.
- **SEO e compartilhamento por página** — meta description, canonical, Open Graph
  e JSON-LD (Person na home, BreadcrumbList nos cases); sitemap e 404 próprios.

Cada página de case documenta as decisões do projeto que descreve — incluindo
as alternativas rejeitadas. Este repositório segue o mesmo princípio.

# douglastassinari.github.io

Site profissional de Douglas Tassinari — **Sistemas de Gestão & Dados**.

Não é um portfólio de inventário: é um argumento em três atos. A home apresenta
a tese ("transformo operações em sistemas de gestão") e três cases a provam,
cada um cobrindo uma natureza diferente do mesmo trabalho:

| Case | Eixo | Prova |
|---|---|---|
| [Plataforma Industrial](https://douglastassinari.github.io/cases/plataforma-industrial/) | Negócio | 0→1 numa indústria real (descrito sem dados sensíveis) |
| [Jornada Brasil](https://douglastassinari.github.io/cases/jornada-brasil/) | Produto | [jornadabrasil.com.br](https://jornadabrasil.com.br) — no ar |
| [Sistema TAZZIN](https://douglastassinari.github.io/cases/tazzin/) | Plataforma | [Demo no ar](https://tazzin.streamlit.app) · [código no GitHub](https://github.com/DouglasTassinari/Tazzin) |

## Estrutura

```
/
├── index.html                      # Home: hero, cases, método, trajetória, stack, contato
├── cases/
│   ├── plataforma-industrial/      # Case 01 · Negócio
│   ├── jornada-brasil/             # Case 02 · Produto
│   ├── tazzin/                     # Case 03 · Plataforma
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
- **Uma folha de CSS para todas as páginas** — tokens em `:root`, sem duplicação;
  as páginas de case compartilham o mesmo template de 7 seções
  (Problema, Contexto, Decisões, Arquitetura, Tecnologias, Resultados, Aprendizados).
- **Diagramas de arquitetura em HTML/CSS** — sem imagem para carregar, legíveis
  por leitor de tela (`role="img"` + `aria-label`), consistentes com o tema.
- **JavaScript como aprimoramento, não dependência** — sem JS o site permanece
  completo e navegável; `prefers-reduced-motion` é respeitado.
- **SEO e compartilhamento por página** — meta description, canonical, Open Graph
  e JSON-LD (Person na home, BreadcrumbList nos cases); sitemap e 404 próprios.

Cada página de case documenta as decisões do projeto que descreve — incluindo
as alternativas rejeitadas. Este repositório segue o mesmo princípio.

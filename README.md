# Pizze Price Scraper

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A web scraping flask app made during the [Queen&#39;s Engineering Competition
(QEC)][qec] in 2018.

[qec]: https://queensengineeringcomp.com/

The code in this repository runs a web application that takes user input of
current address and desired radius. The app uses web scraping to compare the
pizza prices from shops within the input radius, and returns the addresses and
names of the shops with the lowest priced pizzas.

Additional features that would be added with more time on the project are
ability to process and find lowest prices for user specified number of toppings,
number of pizzas, and pizza sizes.

The this repo was originally forked from
<https://github.com/QECProgramming/team3>.

## Install

Prerequisites:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Steps:

```console
git clone https://github.com/bryan-hoang/pizza-price-scraper.git
cd pizza-price-scraper
uv sync
```

## Usage

```console
uv run poe serve
# Visit http://127.0.0.1:5000
```

## Maintainers

- [@bryan-hoang](https://github.com/bryan-hoang)
- [@alcatrazEscapee](https://github.com/alcatrazEscapee)
- [@liam-cregg](https://github.com/liam-cregg)
- [@16zl67](https://github.com/16zl67)

## Contributing

Small note: If editing the README, please conform to the
[standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2018 Bryan Hoang and contributors

# 💱 Conversor de Moedas com Tkinter (API CurrencyLayer)

Aplicação gráfica simples em Python que realiza a conversão de moedas com base em cotações **em tempo real**, usando a API pública [CurrencyLayer](https://currencylayer.com) e interface construída com **Tkinter**.

---

## 🖥️ Funcionalidades

- ✅ Conversão de moedas **para USD** (fixo, conforme plano gratuito da API)
- ✅ Exibição da **última data de atualização** das cotações
- ✅ Interface moderna com Tkinter
- ✅ Lista com as cotações atuais de várias moedas em relação ao dólar
- ✅ Validação de entradas e tratamento de erros de conexão

---

## ⚙️ Tecnologias utilizadas

- `Python`
- `tkinter` (interface gráfica)
- `requests` (requisições HTTP)
- `dotenv` (gestão segura da chave de API)

---

## 📌 Observações
A moeda de destino é fixa em USD, pois o plano gratuito da API CurrencyLayer só permite source=USD.

Para mais moedas ou customização da base, é necessário um plano pago.

O projeto utiliza uma lista manual de moedas populares compatíveis com o plano gratuito.
# Yapay Zeka Uygumaları: Langchain, RAG, LLM Orkestrasyonu

## LLM
- LLM' ler dayandığı **bilimsel çalışma** [Attention Is All You Need](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)  adlı makalede verilmiştir. 
- **Langchain**: Büyük dil modellerini (Large Language Models - LLMs) daha etkili ve pratik bir şekilde kullanmak için geliştirilmiş bir framework'tür. Özellikle, doğal dil işleme tabanlı uygulamalar (chatbotlar, doküman tabanlı sorgulama sistemleri, otomasyon araçları vb.) geliştirenlerin, LLM'lerin gücünden faydalanarak daha dinamik ve karmaşık işlevler sunmasını sağlar. LLM orkestrtasyonu yapar.
- [OpenAI](https://platform.openai.com/) sitesinde bir API Key oluştur.
- [LangChain](https://smith.langchain.com/) sitesinde bir API Key oluştur.
```bash
python -m venv .venv
.venv/Scripts/activate
```
```bash
touch requirements.txt
langchain==0.2.10
langchain-community==0.2.9
langchain-core==0.2.22
langchain-openai==0.1.17
langchain-text-splitters==0.2.2
openai==1.36.0
python-dotenv==1.0.1
fastapi==0.111.1
langserve==0.2.2
sse_starlette==2.1.2
pip install -r requirements.txt
```
```python
touch .env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="..."
LANGCHAIN_PROJECT="..."
```
```bash
touch serve.py
...
python serve.py
http://localhost:8000/chain/playgorund
```
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
python-dotenv
langchain 
langchain-openai
pip install -r requeirements.txt
```
```Python
touch .env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="..."
LANGCHAIN_PROJECT="..."
```
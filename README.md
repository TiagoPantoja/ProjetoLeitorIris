# API Reconhecimento de Íris Python e FastAPI

Este projeto demonstra um sistema de reconhecimento de íris em Python com FastAPI, abordando as etapas de captura da imagem, pré-processamento, extração de características, comparação (matching) e armazenamento de templates.  

---

## Descrição dos Principais Arquivos

- **capture/iris_capture.py**  
  Classe para capturar imagens da câmera.  
  - `IrisCapture`: inicializa a câmera, captura imagens e libera a câmera após uso.

- **preprocessing/iris_preprocessor.py**  
  Classe para pré-processar as imagens de íris.  
  - `IrisPreprocessor`: converte para escala de cinza, aplica equalização de histograma e suavização.

- **feature_extraction/iris_feature_extractor.py**  
  Classe para extrair características de uma imagem de íris (por exemplo, usando PCA).  
  - `IrisFeatureExtractor`: extrai e reduz a dimensionalidade das imagens.

- **matching/iris_matcher.py**  
  Classe para comparar duas amostras (features) de íris.  
  - `IrisMatcher`: usa a distância de Hamming para comparar duas feature vectors.

- **database/in_memory_database.py**  
  Classe para armazenamento em memória de templates de íris.  
  - `InMemoryDatabase`: implementa um simples dicionário para guardar e recuperar templates.

- **models/iris_model.py**  
  Modelo de dados de um template de íris usando Pydantic.  
  - `IrisTemplate`: contém `user_id` e `features`.

- **services/iris_reader_service.py**  
  Classe que orquestra todo o processo de captura, pré-processamento, extração, matching e armazenamento.  
  - `IrisReaderService`: possui métodos como `initialize_camera()`, `enroll_user()`, `identify_user()` e `release_camera()`.

- **data_loader.py**  
  Classe que facilita o carregamento e salvamento de dados externos.  
  - `DataLoader`: inclui métodos para carregar imagens (`load_image_from_file`) e salvar/carregar templates em `.npz` (`save_template_to_file`, `load_template_from_file`).

- **scripts/create_npz_template.py**  
  Exemplo de script para criar arquivos `.npz` contendo `user_id` e `features` para testes de templates.

- **main.py**  
  Exemplo de ponto de entrada da aplicação (caso você deseje colocar endpoints, por exemplo, usando Starlette ou FastAPI).

---

## Requisitos

- Python 3.7+ (idealmente 3.9 ou 3.10)  
- `pip` atualizado (recomendado)

**Bibliotecas Python** (instaladas via `pip` ou `requirements.txt`):  
- [opencv-python](https://pypi.org/project/opencv-python/)  
- [numpy](https://pypi.org/project/numpy/)  
- [scikit-learn](https://pypi.org/project/scikit-learn/)  
- [pydantic](https://pypi.org/project/pydantic/)  
- [starlette](https://pypi.org/project/starlette/) (caso use uma API)  
- [uvicorn](https://pypi.org/project/uvicorn/) (caso use servidor de desenvolvimento)  

> Se houver um arquivo `requirements.txt`, basta rodar:
> ```bash
> pip install -r requirements.txt
> ```

---

## Como Executar

1. **Clonar ou baixar** este repositório na sua máquina local.  
2. **Criar um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # ou no Windows:
   venv\Scripts\activate
   ```

3. **Instalar as dependências**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
    ```
   
4. **Gerar arquivos .npz (opcional):**
    ```bash
    python create_npz_template.py
    ```
Isso criará algo como template_user123.npz.

5. **Executar a aplicação** (caso tenha um `main.py` com endpoints Starlette/FastAPI):
    ```bash
    uvicorn main:app --reload
    ```
- A aplicação estará acessível em http://127.0.0.1:8000/ (por padrão).

6. **Uso básico**:

- Inicializar câmera: chame `IrisReaderService.initialize_camera().`
- Cadastrar usuário (enroll_user): chama `enroll_user("user_id")` para capturar imagem ao vivo, pré-processar, extrair features e salvar no `InMemoryDatabase`.
- Identificar usuário (identify_user): chama `identify_user()` para capturar uma nova imagem e tentar match com os templates existentes.
- Liberar câmera: `release_camera()` quando finalizar.


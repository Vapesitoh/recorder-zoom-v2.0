# ---- Etapa 1: Builder ----
# Usa una imagen completa para instalar dependencias, incluyendo herramientas de compilación
FROM python:3.11-bookworm as builder

WORKDIR /app

# Instala dependencias del sistema operativo necesarias para compilar algunas librerías
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    libegl1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copia solo los archivos de dependencias para aprovechar la caché de Docker
COPY pyproject.toml requirements.txt ./

# Instala las dependencias de Python en un entorno virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir .

# ---- Etapa 2: Final ----
# Usa una imagen slim para la ejecución, mucho más ligera
FROM python:3.11-slim-bookworm

# Crea un usuario no-root para ejecutar la aplicación
RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser

# Copia el entorno virtual con las dependencias desde la etapa de builder
COPY --from=builder /opt/venv /opt/venv

# Copia el código fuente de la aplicación
COPY --chown=appuser:appuser src/ /home/appuser/src

# Establece el entorno para usar el venv
ENV PATH="/opt/venv/bin:$PATH"
ENV QT_QPA_PLATFORM="offscreen"

# Comando para ejecutar la aplicación
CMD ["python", "-m", "focusrecorder"]
.PHONY: all clean

# Variables
ANALYSIS = $(analysis)
DATE = $(shell date +"%Y_%m_%d")
PROJECT = $(DATE)_$(ANALYSIS)

# Default target: create project structure
all: $(PROJECT)

$(PROJECT):
	@echo "Creando estructura de directorios para $(PROJECT)..."
	mkdir -p $(PROJECT)/sql
	touch $(PROJECT)/sql/query.sql
	touch $(PROJECT)/__init__.py
	touch $(PROJECT)/main.py
	touch $(PROJECT)/explore.ipynb
	echo "# $(PROJECT)" > $(PROJECT)/README.md
	@echo "Estructura de directorios y archivos para $(PROJECT) creada."

# Clean target: delete project structure
clean:
	@if [ -n "$(ANALYSIS)" ]; then \
		rm -rf $(DATE)_$(ANALYSIS); \
		echo "Directorio $(DATE)_$(ANALYSIS) eliminado."; \
	else \
		echo "Error: Por favor especifica 'analysis'."; \
	fi
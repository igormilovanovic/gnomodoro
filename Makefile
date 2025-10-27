.PHONY: help install uninstall test run clean

help:
	@echo "Gnomodoro - Pomodoro Timer for GNOME"
	@echo ""
	@echo "Available targets:"
	@echo "  make install    - Install Gnomodoro"
	@echo "  make uninstall  - Uninstall Gnomodoro"
	@echo "  make test       - Run tests"
	@echo "  make run        - Run the application"
	@echo "  make clean      - Clean build artifacts"

install:
	./install.sh

uninstall:
	./uninstall.sh

test:
	python3 -m unittest discover tests -v

run:
	python3 gnomodoro.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build dist *.egg-info

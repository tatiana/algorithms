clean:
	@find . -name "*.pyc" -delete

compare_sorting:
	@python -m comparisons.sorting

install_dependencies:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

test: clean
	@echo "Running all tests..."
	@nosetests -s --with-coverage --cover-erase --cover-inclusive --cover-package=algorithms --tests=tests


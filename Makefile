clean:
	@find . -name "*.pyc" -delete


test: clean
	@echo "Running all tests..."
	@nosetests -s --with-coverage --cover-erase --cover-inclusive --cover-package=algorithms --tests=$(which)


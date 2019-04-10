make:
	@mkdir -p result
	@python3 main.py


test:
	@mkdir -p result
	@bash compare.sh

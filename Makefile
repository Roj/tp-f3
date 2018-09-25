informe: informe.md
	pandoc $^ -o $@.pdf -V geometry:margin=1in


.PHONY: informe

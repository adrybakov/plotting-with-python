.DEFAULT_GOAL := help

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     =
BUILDDIR      = build

help:
	@echo "\x1b[31m"
	@echo "Please specify what do you want to do!"
	@echo "\x1b[0m"
	@echo "Available options are:\n"
	@echo "    help - show this message"
	@echo "    html - build the html docs"
	@echo "    clean - clean all files from docs and pip routines"
	@echo

# $(O) is meant as a shortcut for $(SPHINXOPTS).
html: 
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean-html: clean html
	@echo "Done"


clean:
	-@rm -r docs/build

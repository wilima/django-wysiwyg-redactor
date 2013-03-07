clean:
	@find . -name "*.pyc" -delete

release:
	@sed -ic -e s/`cat VERSION`/$(version)/ setup.py redactor/__init__.py
	@echo $(version) > VERSION
	@git add setup.py VERSION redactor/__init__.py
	@git commit -m "setup: bump to $(version)"
	@git tag $(version)
	@git push --tags
	@git push origin master
	@make clean
	@python setup.py sdist upload
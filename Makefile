shexer_sugarbind:
	python SugarBind/shexer/main.py

update_tag:
	git tag -d v1.0
	git push origin :refs/tags/v10
	git tag v1.0
	git push --tags origin


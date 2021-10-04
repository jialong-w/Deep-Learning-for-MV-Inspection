install: project_venv
	. project_venv/bin/activate; pip3 install -Ur requirements.txt

venv:
	test -d project_venv || python3 -m venv project_venv

run:
	. project_venv/bin/activate; python3 kmeans.py

clean:
	rm -rf project_venv
	find . -iname "*.pyc" -delete

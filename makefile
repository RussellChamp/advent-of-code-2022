default:
	# This is my 2022 Advent of Code project

init:
	mkdir day$(day)
	sed 's/#DAY#/$(day)/g' solve.py.template | sed 's/#TITLE#/$(title)/g' > day$(day)/solve.py
	sed 's/#DAY#/$(day)/g' tests.py.template | sed 's/#TITLE#/$(title)/g' > day$(day)/tests.py
	touch day$(day)/data.txt

run:
	python day$(day)/solve.py

test:
	python day$(day)/tests.py
wc:
	@wc ../day-*/*.py

data:
	yes | head -n 100000 | split

clean:
	rm -f *.{wc,orig,new} x?? LINE-COUNT-SUMMARY

all: data
	@echo Copying...
	./copy.sh x??
	@echo Counting lines...
	./count-lines.sh x??
	@echo Making new file names...
	./new-names.sh x??.wc


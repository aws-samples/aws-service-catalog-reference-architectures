version = 1.1
appname = calc
soname = lib$(appname).so.$(version)

CXXFLAGSShared = -fPIC
CFLAGS = -std=c99

srcfiles = $(wildcard src/*.c)
objects = $(addprefix obj/,$(notdir $(srcfiles:.c=.o)))

$(appname): $(objects)
	mkdir -p bin/     
	gcc -shared $(CFLAGS) $(CXXFLAGSShared) -Wl,-soname,$(soname) -o bin/$(soname) $(objects) -lc
	ln -sf $(soname) bin/lib$(appname).so

obj/%.o: src/%.c
	mkdir -p obj/
	gcc $(CFLAGS) $(CXXFLAGSShared) -c $< -o $@

test:
	gcc $(CFLAGS) -Wl,-R -Wl,bin/ test.c bin/lib$(appname).so -o calctest
	./calctest

all: $(appname) test

clean: .clean $(appname)
cleanall: .clean all
cleanonly: .clean
.clean:
	rm -rf obj
	rm -rf bin
	rm -rf flaskapp
	rm -f calctest
	rm -rf build build.zip
	rm -f flaskapp.zip
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type d -name __pycache__ -delete
	rm -rf __pycache__

docker: .copyfiles

lambda: clean
	mkdir -p build/
	cp -r pycalc build
	cp -r bin build
	cp lambda_function.py build
	cd build; zip -9qr ../build.zip *
	#rm -rf build

.copyfiles: cleanall
	mkdir -p flaskapp
	cp flask/requirements.txt ./flaskapp
	cp flask/application.py ./flaskapp	
	cp -r pycalc flaskapp
	cp -r bin flaskapp

local: .copyfiles
	cp flask/rungunicorn.sh ./flaskapp	
	cp flask/gu.local ./flaskapp/gu.py
	cd ./flaskapp; ./rungunicorn.sh
	
eb: .copyfiles
	cp flask/gu.conf ./flaskapp/gu.py	
	cd flaskapp; zip -9qr ../build.zip *

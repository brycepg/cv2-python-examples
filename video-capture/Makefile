files=drop.avi video-capture-example.py
folder=video-capture
ver=1.0
zip=$(folder)-$(ver).zip

zip: $(zip)

$(zip):$(files)
	mkdir -p $(folder)
	cp $(files) $(folder)
	zip -r $(zip) $(folder)

clean:
	rm -r $(folder)

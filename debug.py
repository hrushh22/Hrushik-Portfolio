f = open('index.html', 'rb')
content = f.read().decode('utf-8')
f.close()

# Print hero section HTML
hero_start = content.find('<section id="hero">')
hero_end = content.find('</section>', hero_start) + 10
print("=== HERO HTML ===")
print(content[hero_start:hero_end])

# Print photo wrap CSS
css_start = content.find('.hero-photo-wrap')
print("\n=== PHOTO WRAP CSS ===")
print(content[css_start:css_start+300])

# Print hero-inner CSS
inner_start = content.find('.hero-inner')
print("\n=== HERO INNER CSS ===")
print(content[inner_start:inner_start+200])

# Print #hero CSS
hero_css = content.find('#hero {')
print("\n=== #HERO CSS ===")
print(content[hero_css:hero_css+200])

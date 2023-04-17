import re

languages_scripts = {
    'python': '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js" integrity="sha512-AKaNmg8COK0zEbjTdMHJAPJ0z6VeNqvRvH4/d5M4sHJbQQUToMBtodq4HaV4fa+WV2UTfoperElm66c9/8cKmQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>',
    'bash': '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js" integrity="sha512-whYhDwtTmlC/NpZlCr6PSsAaLOrfjVg/iXAnC4H/dtiHawpShhT2SlIMbpIhT/IL/NrpdMm+Hq2C13+VKpHTYw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>',
    'css': '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-css.min.js" integrity="sha512-uMdVuOpm+9lNPCT7mV/YaMb9YQ/R4+eeON7aEMj6Ig/f4BoU+Q5k6iaZkDsX7LH9cjTHZt0CuKxbzd0/fndrWA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>',
    'html': '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-cshtml.min.js" integrity="sha512-2wQgFnVoaXxggU4WP6nmo8W15z91WyQOor7iapCRfycFWoAU3fqRfoJfoO5oNg5kl94fGgFlyeHxOcqgjEvaAQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>',
    'javascript': '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.js" integrity="sha512-Kz83UzPU5O1qUHKfcuwW6tsPfSlGoAR7GIrdRh5oPOM/M2qphGQJOGfPVjQHk/D1TwkhltYvQjLqW/DErTc9rw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>',
    'cpp': '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-cpp.min.js" integrity="sha512-namzGTZvHaug0jeipHRN2pMepMiJj+EbrloktVFlMYGnA0EwZhbdLeENjBYLCgoghVbZGinIz/FFYHmB0o3wLw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>',
    'arduino': '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-arduino.min.js" integrity="sha512-ljFCRrpgOuJ0NcKClrnDFGRIEeq45+VB2vThzShgXKP464zVRGmK8jLpRZAiD5xIpQnxekVcwDPWVvX2yKPnHQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>',
    'md': '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-markdown.min.js" integrity="sha512-IHQR8J+JbQpZ1tjkHkq8Ivsgo6ovfnYbQnYzmoKCjTCQG90YVs9l+2P14DRIZ94VBrB+F86Ju4wSGOMOjfVCQQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>'
}

autoloader_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js" integrity="sha512-SkmBfuA2hqjzEVpmnMt/LINrjop3GKWqsuLSSB3e7iBmYK7JuWw4ldmmxwD9mdm2IRTTi0OxSAfEGvgEi0i2Kw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>'

main_prism_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>'

css_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />'

def add_prismjs(content):
    # find all language-xxx classes and get the xxx parts in a list
    languages = re.findall(r'language-([a-z0-9-]+)', content)
    # remove duplicates
    languages = list(set(languages))
    # sort the list
    languages.sort()
    # add the scripts
    toadd = ''
    for language in languages:
        toadd += languages_scripts[language] + '\n' if language in languages_scripts else ''
    content = content.replace('</head>', f'\n{main_prism_script}\n{autoloader_script}\n{css_link}\n{toadd}</head>') if toadd else content
    return content
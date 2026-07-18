import os
import json
import re

files = ["index.html", "platform.html", "events.html", "event-guildhall.html", "event-field.html"]

dictionary = {}

def add_translation(key, val):
    dictionary[key] = val
    return f'data-i18n="{key}"'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if file == "index.html":
        content = content.replace('class="nav-name">Social Democratic Alliance<', 'class="nav-name" data-i18n="nav-name">Social Democratic Alliance<')
        dictionary["nav-name"] = "Social Democratic Alliance"
        
        content = content.replace('<li><a href="index.html" class="active">Home</a></li>', '<li><a href="index.html" class="active" data-i18n="nav-home">Home</a></li>')
        content = content.replace('<li><a href="platform.html">Platform</a></li>', '<li><a href="platform.html" data-i18n="nav-platform">Platform</a></li>')
        content = content.replace('<li><a href="events.html">Campaigning</a></li>', '<li><a href="events.html" data-i18n="nav-campaigning">Campaigning</a></li>')
        dictionary["nav-home"] = "Home"
        dictionary["nav-platform"] = "Platform"
        dictionary["nav-campaigning"] = "Campaigning"

        content = content.replace('<div class="hero-eyebrow" style="font-size: 1.1rem; color: var(--primary); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 20px;">Social Democratic Alliance</div>', '<div class="hero-eyebrow" data-i18n="idx-eyebrow" style="font-size: 1.1rem; color: var(--primary); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 20px;">Social Democratic Alliance</div>')
        dictionary["idx-eyebrow"] = "Social Democratic Alliance"

        content = content.replace('<h1 class="hero-title" style="font-size: clamp(3.5rem, 6vw, 6rem); line-height: 1.05; margin-bottom: 24px; ">Aldric von Reichel <br/><span style="color: var(--primary);">for Cambria</span></h1>', '<h1 class="hero-title" data-i18n="idx-hero-title" style="font-size: clamp(3.5rem, 6vw, 6rem); line-height: 1.05; margin-bottom: 24px; ">Aldric von Reichel <br/><span style="color: var(--primary);">for Cambria</span></h1>')
        dictionary["idx-hero-title"] = 'Aldric von Reichel <br/><span style="color: var(--primary);">for Cambria</span>'

        content = content.replace('<p class="hero-subtitle" style="font-size: 1.35rem; line-height: 1.6; color: var(--text-muted); margin-bottom: 40px; max-width: 600px;">A campaign for the working masses. I am fighting for a Cambria where every small business can thrive and every rural town is connected - built on the unbreakable foundations of our republic.</p>', '<p class="hero-subtitle" data-i18n="idx-hero-sub" style="font-size: 1.35rem; line-height: 1.6; color: var(--text-muted); margin-bottom: 40px; max-width: 600px;">A campaign for the working masses. I am fighting for a Cambria where every small business can thrive and every rural town is connected - built on the unbreakable foundations of our republic.</p>')
        dictionary["idx-hero-sub"] = "A campaign for the working masses. I am fighting for a Cambria where every small business can thrive and every rural town is connected - built on the unbreakable foundations of our republic."

        content = content.replace('<a href="platform.html" class="btn-primary" style="text-decoration: none; padding: 16px 36px; font-size: 1.15rem;">The Cambria Platform</a>', '<a href="platform.html" class="btn-primary" data-i18n="idx-btn-plat" style="text-decoration: none; padding: 16px 36px; font-size: 1.15rem;">The Cambria Platform</a>')
        dictionary["idx-btn-plat"] = "The Cambria Platform"

        content = content.replace('<a href="events.html" class="btn-outline" style="text-decoration: none; padding: 16px 36px; font-size: 1.15rem;">On the Trail</a>', '<a href="events.html" class="btn-outline" data-i18n="idx-btn-events" style="text-decoration: none; padding: 16px 36px; font-size: 1.15rem;">On the Trail</a>')
        dictionary["idx-btn-events"] = "On the Trail"

        content = content.replace('<h2 style="font-size: 2.5rem;  margin-bottom: 15px; font-family: \'Outfit\', sans-serif;">Our Vision for Cambria</h2>', '<h2 data-i18n="idx-vision-title" style="font-size: 2.5rem;  margin-bottom: 15px; font-family: \'Outfit\', sans-serif;">Our Vision for Cambria</h2>')
        dictionary["idx-vision-title"] = "Our Vision for Cambria"

        content = content.replace('<p style="opacity: 0.9; font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.5;">Our campaign is built on tangible commitments to the people of Cambria. From defending local businesses against monopolies and securing fair contracts, to investing in critical rail infrastructure and agricultural research, we are fighting for an economy that empowers everyone.</p>', '<p data-i18n="idx-vision-desc" style="opacity: 0.9; font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.5;">Our campaign is built on tangible commitments to the people of Cambria. From defending local businesses against monopolies and securing fair contracts, to investing in critical rail infrastructure and agricultural research, we are fighting for an economy that empowers everyone.</p>')
        dictionary["idx-vision-desc"] = "Our campaign is built on tangible commitments to the people of Cambria. From defending local businesses against monopolies and securing fair contracts, to investing in critical rail infrastructure and agricultural research, we are fighting for an economy that empowers everyone."

        bento_items = [
            ("Anti-Monopoly", "Mandatory reviews for mergers to protect local businesses.", "idx-b1"),
            ("Contract Protections", "Sector minimums to prevent predatory agreements.", "idx-b2"),
            ("Local Rail Node", "Dedicated connectivity built with Cambria\'s zoning authority.", "idx-b3"),
            ("Cambrian R&D Center", "Regional research prioritizing local soil, crops, and talent.", "idx-b4"),
            ("Freight Capacity", "Timed to local harvest and production cycles.", "idx-b5"),
            ("Collective Bargaining", "Legal safeguards protecting the right to organize.", "idx-b6")
        ]
        
        for i, (title, desc, key) in enumerate(bento_items):
            content = content.replace(f'<h3 style="font-size: 1.2rem; margin-bottom: 4px; font-family: \'Outfit\', sans-serif; ">{title}</h3>', f'<h3 data-i18n="{key}-t" style="font-size: 1.2rem; margin-bottom: 4px; font-family: \'Outfit\', sans-serif; ">{title}</h3>')
            content = content.replace(f'<p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.4; margin: 0;">{desc}</p>', f'<p data-i18n="{key}-d" style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.4; margin: 0;">{desc}</p>')
            dictionary[f"{key}-t"] = title
            dictionary[f"{key}-d"] = desc

    if file == "platform.html":
        content = content.replace('class="nav-name">Social Democratic Alliance<', 'class="nav-name" data-i18n="nav-name">Social Democratic Alliance<')
        content = content.replace('<li><a href="index.html">Home</a></li>', '<li><a href="index.html" data-i18n="nav-home">Home</a></li>')
        content = content.replace('<li><a href="platform.html" class="active">Platform</a></li>', '<li><a href="platform.html" class="active" data-i18n="nav-platform">Platform</a></li>')
        content = content.replace('<li><a href="events.html">Campaigning</a></li>', '<li><a href="events.html" data-i18n="nav-campaigning">Campaigning</a></li>')

        content = content.replace('<h1 style=" font-size: 4.5rem;">The Cambria Platform</h1>', '<h1 data-i18n="plat-title" style=" font-size: 4.5rem;">The Cambria Platform</h1>')
        dictionary["plat-title"] = "The Cambria Platform"
        
        content = content.replace('<p style="margin: 0 auto; font-size: 1.25rem; max-width: 600px;">We are building an economy that rewards those who build it, by hand and by brain, ending the exploitation by monopolies.</p>', '<p data-i18n="plat-desc" style="margin: 0 auto; font-size: 1.25rem; max-width: 600px;">We are building an economy that rewards those who build it, by hand and by brain, ending the exploitation by monopolies.</p>')
        dictionary["plat-desc"] = "We are building an economy that rewards those who build it, by hand and by brain, ending the exploitation by monopolies."

        plat_items = [
            ("Anti-Monopoly Enforcement", "Automatic review triggers for mergers to protect local suppliers.", "plat-b1"),
            ("Regional Contracts", "Minimum terms by sector preventing predatory agreements.", "plat-b2"),
            ("High-Speed Rail Node", "Dedicated connection retaining local zoning authority.", "plat-b3"),
            ("Cambrian R&D Center", "Regional center prioritizing local soil, crops, and talent.", "plat-b4"),
            ("Freight Capacity", "Timed to local harvest and production cycles.", "plat-b5"),
            ("Collective Bargaining", "Real enforcement behind the right to organize and strike.", "plat-b6")
        ]
        
        for i, (title, desc, key) in enumerate(plat_items):
            content = content.replace(f'<h3 style="font-size: 1.2rem; margin-bottom: 4px; font-family: \'Outfit\', sans-serif; ">{title}</h3>', f'<h3 data-i18n="{key}-t" style="font-size: 1.2rem; margin-bottom: 4px; font-family: \'Outfit\', sans-serif; ">{title}</h3>')
            content = content.replace(f'<p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.4; margin: 0;">{desc}</p>', f'<p data-i18n="{key}-d" style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.4; margin: 0;">{desc}</p>')
            dictionary[f"{key}-t"] = title
            dictionary[f"{key}-d"] = desc
            
            content = content.replace(f'<h3 style="font-family: \'Outfit\', sans-serif;">{title}</h3>', f'<h3 data-i18n="{key}-mt" style="font-family: \'Outfit\', sans-serif;">{title}</h3>')
            dictionary[f"{key}-mt"] = title

        m1 = '"People who\'d actually notice three delivery firms becoming one, before the paperwork was finalized instead of after, when it is late to fix it... This law would establish the door into monopolies slower. And a slower door is time you don\'t currently have."'
        m2 = '"Minimum contract terms set by sector, renegotiated with regional input rather than dictated by whoever has the largest share of the route in question. A buyer can still choose not to work with you. They cannot use the absence of alternatives as leverage to set terms below that floor."'
        m3 = '"The connection runs both ways, or it isn\'t worth building... Zoning and development around the node stay under Cambria\'s own authority, not handed to a regional planning board seated in the capital. You get the connection. You don\'t lose the town to it."'
        m4 = '"An institution that answers to this town and its people before it answers to anyone else... Funded positions here, reserved for Cambrian applicants first, with the university stipends to make it possible for someone from this town to train and come home to something worth coming home to."'
        m5 = '"Freight capacity for the feed exchange and the textile cooperative both, timed to your harvest and production cycles rather than a fixed citywide schedule designed around the convenience of others. A stop that exists because Cambria has cargo worth stopping for, or so I believe your cargo is worth stopping for."'
        m6 = '"Monopoly does not care whether the hand it closes belongs to a shop owner or a shift worker. It closes on both."'

        modals = [m1, m2, m3, m4, m5, m6]
        for i, text in enumerate(modals):
            content = content.replace(f'<p style="font-style: italic; color: var(--text-muted); font-size: 1.1rem; line-height: 1.7;">{text}</p>', f'<p data-i18n="plat-b{i+1}-md" style="font-style: italic; color: var(--text-muted); font-size: 1.1rem; line-height: 1.7;">{text}</p>')
            dictionary[f"plat-b{i+1}-md"] = text

        content = content.replace('<p style="margin-top: 10px; font-weight: 600; text-align: right;">— Aldric von Reichel</p>', '<p data-i18n="plat-quote-author" style="margin-top: 10px; font-weight: 600; text-align: right;">- Aldric von Reichel</p>')
        dictionary["plat-quote-author"] = "- Aldric von Reichel"

    if file == "events.html":
        content = content.replace('class="nav-name">Social Democratic Alliance<', 'class="nav-name" data-i18n="nav-name">Social Democratic Alliance<')
        content = content.replace('<li><a href="index.html">Home</a></li>', '<li><a href="index.html" data-i18n="nav-home">Home</a></li>')
        content = content.replace('<li><a href="platform.html">Platform</a></li>', '<li><a href="platform.html" data-i18n="nav-platform">Platform</a></li>')
        content = content.replace('<li><a href="events.html" class="active">Campaigning</a></li>', '<li><a href="events.html" class="active" data-i18n="nav-campaigning">Campaigning</a></li>')

        content = content.replace('<h1 style=" font-size: 4.5rem;">On the Trail</h1>', '<h1 data-i18n="ev-title" style=" font-size: 4.5rem;">On the Trail</h1>')
        dictionary["ev-title"] = "On the Trail"

        content = content.replace('<p style="margin: 0 auto; font-size: 1.25rem; max-width: 600px;">Follow Aldric von Reichel on the campaign trail as we bring the platform to every corner of Cambria.</p>', '<p data-i18n="ev-desc" style="margin: 0 auto; font-size: 1.25rem; max-width: 600px;">Follow Aldric von Reichel on the campaign trail as we bring the platform to every corner of Cambria.</p>')
        dictionary["ev-desc"] = "Follow Aldric von Reichel on the campaign trail as we bring the platform to every corner of Cambria."

        content = content.replace('<h2 class="section-title" style="margin-bottom: 40px;">Campaign Material</h2>', '<h2 data-i18n="ev-mat-title" class="section-title" style="margin-bottom: 40px;">Campaign Material</h2>')
        dictionary["ev-mat-title"] = "Campaign Material"

        content = content.replace('>Download Campaigning Material (DOCX)<', ' data-i18n="ev-mat-dl">Download Campaigning Material (DOCX)<')
        dictionary["ev-mat-dl"] = "Download Campaigning Material (DOCX)"

        content = content.replace('<h2 class="news-title" style="font-family: \'Outfit\', sans-serif;  margin-bottom: 15px;">Built Around Cambria</h2>', '<h2 data-i18n="ev-card1-t" class="news-title" style="font-family: \'Outfit\', sans-serif;  margin-bottom: 15px;">Built Around Cambria</h2>')
        dictionary["ev-card1-t"] = "Built Around Cambria"

        card1_desc = "Aldric von Reichel meets with Governess Wren and local shop owners at the guildhall. He outlines his platform for anti-monopoly enforcement, regional contract protections, and bringing a dedicated R&D center directly to Cambria."
        content = content.replace(f'<p class="news-excerpt" style="color: var(--text-muted); line-height: 1.6;">{card1_desc}</p>', f'<p data-i18n="ev-card1-d" class="news-excerpt" style="color: var(--text-muted); line-height: 1.6;">{card1_desc}</p>')
        dictionary["ev-card1-d"] = card1_desc

        content = content.replace('<h2 class="news-title" style="font-family: \'Outfit\', sans-serif;  margin-bottom: 15px;">The Line Runs Both Ways</h2>', '<h2 data-i18n="ev-card2-t" class="news-title" style="font-family: \'Outfit\', sans-serif;  margin-bottom: 15px;">The Line Runs Both Ways</h2>')
        dictionary["ev-card2-t"] = "The Line Runs Both Ways"

        card2_desc = "Speaking with workers in the field and locals at the town well, Aldric details the High-Speed Rail node plan. He commits to ensuring the node connects Cambria without surrendering local zoning authority to larger districts."
        content = content.replace(f'<p class="news-excerpt" style="color: var(--text-muted); line-height: 1.6;">{card2_desc}</p>', f'<p data-i18n="ev-card2-d" class="news-excerpt" style="color: var(--text-muted); line-height: 1.6;">{card2_desc}</p>')
        dictionary["ev-card2-d"] = card2_desc

        content = content.replace('>Read Full Story<', ' data-i18n="ev-read-full">Read Full Story<')
        dictionary["ev-read-full"] = "Read Full Story"

    if file in ["event-guildhall.html", "event-field.html"]:
        content = content.replace('class="nav-name">Social Democratic Alliance<', 'class="nav-name" data-i18n="nav-name">Social Democratic Alliance<')
        content = content.replace('<li><a href="index.html">Home</a></li>', '<li><a href="index.html" data-i18n="nav-home">Home</a></li>')
        content = content.replace('<li><a href="platform.html">Platform</a></li>', '<li><a href="platform.html" data-i18n="nav-platform">Platform</a></li>')
        content = content.replace('<li><a href="events.html" class="active">Campaigning</a></li>', '<li><a href="events.html" class="active" data-i18n="nav-campaigning">Campaigning</a></li>')

        content = content.replace('>Back to Trail<', ' data-i18n="ev-back">Back to Trail<')
        dictionary["ev-back"] = "Back to Trail"
        
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        prefix = "gh" if file == "event-guildhall.html" else "fl"
        
        h1 = soup.find('h1')
        if h1 and not h1.has_attr('data-i18n'):
            h1['data-i18n'] = f"{prefix}-title"
            dictionary[f"{prefix}-title"] = h1.decode_contents()

        page_header = soup.find('section', class_='page-header')
        if page_header:
            p_sub = page_header.find('p')
            if p_sub and not p_sub.has_attr('data-i18n'):
                p_sub['data-i18n'] = f"{prefix}-sub"
                dictionary[f"{prefix}-sub"] = p_sub.decode_contents()

        news_section = soup.find('section', class_='news-section')
        if news_section:
            ps = news_section.find_all('p', recursive=False)
            for idx, p in enumerate(ps):
                if not p.has_attr('data-i18n'):
                    key = f"{prefix}-p{idx+1}"
                    p['data-i18n'] = key
                    dictionary[key] = p.decode_contents()

        content = str(soup)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

with open('new_source.json', 'w', encoding='utf-8') as f:
    json.dump(dictionary, f, indent=2, ensure_ascii=False)

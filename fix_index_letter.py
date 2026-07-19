import re

with open('index.html', 'r') as f:
    content = f.read()

# Find the start of the latest-trail-section
match_start = re.search(r'  <section class="latest-trail-section".*?>', content)
if match_start:
    start_idx = match_start.start()
    
    # Find the closing tag
    match_end = re.search(r'  </section>', content[start_idx:])
    if match_end:
        end_idx = start_idx + match_end.end()
        
        new_section = """  <section class="letter-section" style="position: relative; z-index: 5; padding: 80px 5%; max-width: 900px; margin: 0 auto;">
    <div style="text-align: center; margin-bottom: 40px;">
      <span style="color: var(--primary); font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.9rem; display: block; margin-bottom: 10px;" data-i18n="idx-letter-eyebrow">A Message from Aldric</span>
      <h2 data-i18n="idx-letter-title" style="font-family: 'Outfit', sans-serif; font-size: 2.8rem; margin: 0; color: var(--text-main);">A Letter to Cambria</h2>
    </div>

    <div class="letter-card" style="background: var(--glass-bg); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid var(--glass-border); border-radius: var(--radius-xl); padding: 60px 80px; box-shadow: 0 15px 50px rgba(0,0,0,0.06); position: relative; overflow: hidden; border-top: 6px solid var(--primary);">
      
      <!-- Subtle quotation mark watermark -->
      <div style="position: absolute; top: 10px; left: 30px; opacity: 0.04; font-family: 'Playfair Display', serif; font-size: 15rem; line-height: 1; color: var(--primary); user-select: none;">
        "
      </div>

      <div style="position: relative; z-index: 2; font-family: 'Playfair Display', serif; font-size: 1.35rem; color: var(--text-main); line-height: 1.8;">
        <p data-i18n="idx-letter-p1" style="margin-bottom: 24px;">The tragedy that brought us to this by-election is a shadow over our republic. The loss of MP Richard Balls reminds us of the stakes we face. But while the politicians in Montiablo argue over power, the rural communities of Cambria are left behind.</p>
        
        <p data-i18n="idx-letter-p2" style="margin-bottom: 24px;">We are watching our local businesses get swallowed by monopolies. We are watching our young people leave because the investment stops at the city limits.</p>
        
        <p data-i18n="idx-letter-p3" style="margin-bottom: 40px; font-weight: 600; color: var(--primary);">I am running because Cambria deserves a voice that cannot be bought. We are going to build a future grounded in our own soil, protected by our own laws, and run by our own people. Join us. Let us rebuild.</p>
        
        <div style="margin-top: 40px; border-top: 1px solid var(--border-color); padding-top: 30px; display: flex; align-items: center; gap: 20px;">
          <img src="AldricvonReichelPortraitNoBG.png" alt="Aldric von Reichel" style="width: 70px; height: 70px; border-radius: 50%; object-fit: cover; border: 2px solid var(--primary); background: var(--bg-body);">
          <div>
            <div style="font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 1.3rem; color: var(--text-main); line-height: 1.2;">Aldric von Reichel</div>
            <div style="font-size: 0.95rem; color: var(--text-muted); font-family: 'Inter', sans-serif;">SDA Candidate for Chasmia</div>
          </div>
        </div>
      </div>
    </div>
  </section>"""
        
        # Replace the entire block
        new_content = content[:start_idx] + new_section + content[end_idx:]
        
        with open('index.html', 'w') as f:
            f.write(new_content)
        print("Successfully updated index.html")
    else:
        print("Could not find closing </section>")
else:
    print("Could not find start of latest-trail-section")


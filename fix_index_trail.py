import re

with open('index.html', 'r') as f:
    content = f.read()

# Find the start of the crisis section
match_start = re.search(r'  <section class="crisis-section".*?>', content)
if match_start:
    start_idx = match_start.start()
    
    # Find the closing tag of the crisis section
    match_end = re.search(r'  </section>', content[start_idx:])
    if match_end:
        end_idx = start_idx + match_end.end()
        
        new_trail_section = """  <section class="latest-trail-section" style="position: relative; z-index: 5; padding: 60px 5%; max-width: 1000px; margin: 0 auto;">
    <div style="text-align: center; margin-bottom: 40px;">
      <span style="color: var(--primary); font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.9rem; display: block; margin-bottom: 10px;">Latest Update</span>
      <h2 data-i18n="ev-title" style="font-family: 'Outfit', sans-serif; font-size: 2.5rem; margin: 0; color: var(--text-main);">On the Trail</h2>
    </div>

    <a href="event-guildhall.html" style="text-decoration: none; display: block;">
      <div class="trail-card" style="background: var(--glass-bg); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid var(--glass-border); border-radius: var(--radius-xl); padding: 50px; box-shadow: 0 10px 40px rgba(0,0,0,0.03); display: flex; flex-direction: column; gap: 20px; transition: transform 0.4s ease, box-shadow 0.4s ease, border-color 0.4s ease; position: relative; overflow: hidden; border-left: 4px solid var(--primary);">
        
        <style>
          .trail-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(215, 0, 58, 0.1) !important;
            border-color: rgba(215, 0, 58, 0.2) !important;
          }
          .trail-card:hover .trail-btn {
            background: var(--primary-hover);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(215, 0, 58, 0.3);
          }
        </style>

        <div style="position: absolute; top: -20px; right: -20px; opacity: 0.03; transform: rotate(15deg);">
          <svg viewBox="0 0 24 24" width="200" height="200" fill="var(--primary)"><path d="M12 2L2 22h20L12 2zm0 3.8l7.2 14.2H4.8L12 5.8z"/></svg>
        </div>

        <div style="position: relative; z-index: 2;">
          <h3 data-i18n="gh-title" style="font-family: 'Playfair Display', serif; font-size: 2.4rem; color: var(--text-main); margin-bottom: 8px; line-height: 1.2;">"Built Around Cambria"</h3>
          <p data-i18n="gh-sub" style="font-size: 1.15rem; color: var(--primary); font-weight: 600; margin-bottom: 24px;">Aldric von Reichel visits the guildhall of Cambria.</p>
          
          <p data-i18n="gh-p1" style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 32px; max-width: 800px;">The guildhall smelled of old paper, the kind of smell that came from a building that has been actively used by the local community. Aldric von Reichel had walked the market street before coming inside, four shopfronts without any cameras trailing him. A shoemaker had shown him a boot he was proud of. A grocer had complained about delivery contracts that always seemed to favor whoever already had the most trucks. By the time he reached the guildhall, he had heard the shape of the argument he was about to have before anyone in the room had said a word.</p>
          
          <div class="trail-btn btn-primary" data-i18n="ev-read-full" style="padding: 14px 32px; font-size: 1.05rem; display: inline-flex; align-items: center; justify-content: center; font-weight: 600; border-radius: var(--radius-sm); transition: var(--transition);">Read Full Story</div>
        </div>
      </div>
    </a>
  </section>"""
        
        # Replace the entire block
        new_content = content[:start_idx] + new_trail_section + content[end_idx:]
        
        with open('index.html', 'w') as f:
            f.write(new_content)
        print("Successfully updated index.html")
    else:
        print("Could not find closing </section>")
else:
    print("Could not find start of crisis-section")


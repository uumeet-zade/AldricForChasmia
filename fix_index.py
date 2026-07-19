import re

with open('index.html', 'r') as f:
    content = f.read()

# The bento-grid section starts at <section class="bento-grid" ...>
# Inside it, there is "Our Vision for Cambria".
# After the closing </div> of the bento-full intro card, we should close the section.

new_banner = """  </section>

  <section class="crisis-section" style="position: relative; z-index: 5; padding: 0 5%; max-width: 1400px; margin: 0 auto;">
    <!-- Premium Crisis Banner -->
    <style>
      .premium-crisis-banner {
        position: relative;
        padding: 60px 40px;
        background: linear-gradient(135deg, rgba(215, 0, 58, 0.05) 0%, rgba(0,0,0,0) 100%);
        border-top: 1px solid rgba(215, 0, 58, 0.2);
        border-bottom: 1px solid rgba(215, 0, 58, 0.2);
        margin: 40px auto;
        overflow: hidden;
        border-radius: var(--radius-lg);
      }
      .premium-crisis-banner::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at center, rgba(215,0,58,0.03) 0%, transparent 50%);
        animation: pulseGlow 10s infinite linear;
        pointer-events: none;
      }
      @keyframes pulseGlow {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }
      .crisis-banner-header {
        text-align: center;
        margin-bottom: 40px;
        position: relative;
        z-index: 2;
      }
      .crisis-banner-eyebrow {
        color: var(--primary);
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-size: 0.9rem;
        margin-bottom: 10px;
        display: block;
      }
      .crisis-cards-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 24px;
        position: relative;
        z-index: 2;
      }
      .crisis-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: var(--radius-xl);
        padding: 32px 24px;
        text-align: left;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        display: flex;
        flex-direction: column;
      }
      .crisis-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, var(--primary), #ff4d6d);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      }
      .crisis-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(215, 0, 58, 0.1);
        border-color: rgba(215, 0, 58, 0.3);
      }
      .crisis-card:hover::before {
        transform: scaleX(1);
      }
      .crisis-card-icon {
        width: 56px;
        height: 56px;
        background: rgba(215, 0, 58, 0.08);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 24px;
        color: var(--primary);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      }
      .crisis-card:hover .crisis-card-icon {
        background: var(--primary);
        color: white;
        transform: scale(1.15) rotate(10deg);
        box-shadow: 0 8px 20px rgba(215, 0, 58, 0.3);
      }
      .crisis-card h3 {
        font-family: 'Outfit', sans-serif;
        font-size: 1.3rem;
        color: var(--text-main);
        margin-bottom: 12px;
        transition: color 0.3s ease;
      }
      .crisis-card:hover h3 {
        color: var(--primary);
      }
      .crisis-card p {
        font-size: 0.95rem;
        color: var(--text-muted);
        line-height: 1.6;
        margin: 0;
      }
    </style>

    <div class="premium-crisis-banner">
      <div class="crisis-banner-header">
        <span class="crisis-banner-eyebrow" data-i18n="idx-eyebrow-crisis">Our Commitment</span>
        <h2 style="font-family: 'Outfit', sans-serif; font-size: 2.2rem; margin: 0; color: var(--text-main);">The Cambria Pledge</h2>
      </div>
      
      <div class="crisis-cards-container">
        <!-- Card 1 -->
        <div class="crisis-card">
          <div class="crisis-card-icon">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z"/></svg>
          </div>
          <h3 data-i18n="idx-b1-t">Anti-Monopoly</h3>
          <p data-i18n="idx-b1-d">Mandatory reviews for mergers to protect local businesses.</p>
        </div>

        <!-- Card 2 -->
        <div class="crisis-card">
          <div class="crisis-card-icon">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
          </div>
          <h3 data-i18n="idx-b2-t">Contract Protections</h3>
          <p data-i18n="idx-b2-d">Sector minimums to prevent predatory agreements.</p>
        </div>

        <!-- Card 3 -->
        <div class="crisis-card">
          <div class="crisis-card-icon">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M12 2c-4.42 0-8 .5-8 4v9.5C4 17.43 5.57 19 7.5 19L6 20.5v.5h12v-.5L16.5 19c1.93 0 3.5-1.57 3.5-3.5V6c0-3.5-3.58-4-8-4zM7.5 17c-.83 0-1.5-.67-1.5-1.5S6.67 14 7.5 14s1.5.67 1.5 1.5S8.33 17 7.5 17zm3.5-7H6V6h5v4zm4 0V6h5v4h-5zm1.5 7c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>
          </div>
          <h3 data-i18n="idx-b3-t">Local Rail Node</h3>
          <p data-i18n="idx-b3-d">Dedicated connectivity built with Cambria's zoning authority.</p>
        </div>

        <!-- Card 4 -->
        <div class="crisis-card">
          <div class="crisis-card-icon">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7z"/></svg>
          </div>
          <h3 data-i18n="idx-b4-t">Cambrian R&D Center</h3>
          <p data-i18n="idx-b4-d">Regional research prioritizing local soil, crops, and talent.</p>
        </div>
      </div>
    </div>
  </section>
"""

# Find the start of the 6 Campaign Promises comment
match_start = re.search(r'    <!-- 6 Campaign Promises', content)
if match_start:
    start_idx = match_start.start()
    
    # Find the closing tag of the bento-grid section
    # Let's search from start_idx for the NEXT </section>
    match_end = re.search(r'  </section>', content[start_idx:])
    if match_end:
        end_idx = start_idx + match_end.end()
        
        # Replace the entire block
        new_content = content[:start_idx] + new_banner + content[end_idx:]
        
        with open('index.html', 'w') as f:
            f.write(new_content)
        print("Successfully updated index.html")
    else:
        print("Could not find closing </section>")
else:
    print("Could not find start of 6 Campaign Promises")


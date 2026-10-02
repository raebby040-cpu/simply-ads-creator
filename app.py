import gradio as gr
import tempfile
import os


# ============================================================
# SIMPLE ADS CREATOR BY RAYMOND
# Multi-platform advertising script generator
#
# Platforms:
# TikTok
# Instagram
# Facebook
# WhatsApp Status
# YouTube Shorts
# WhatsApp
# General Online Ad
#
# No paid APIs.
# No API keys.
# Python + Gradio only.
# ============================================================


APP_NAME = "Simple Ads Creator by Raymond"

# ------------------------------------------------------------
# PRO UNLOCK CODES
# ------------------------------------------------------------

UNLOCK_CODES = {
    "RAYMOND2026",
    "SIMPLE20K",
}


# ------------------------------------------------------------
# PLATFORM INFORMATION
# ------------------------------------------------------------

PLATFORM_GUIDANCE = {
    "TikTok": {
        "hook": "Make the first 2 seconds impossible to ignore.",
        "length": "15–45 seconds",
        "cta": "Tell viewers to DM or WhatsApp immediately."
    },

    "Instagram Reels": {
        "hook": "Start with a visually strong hook and short statement.",
        "length": "15–60 seconds",
        "cta": "Ask viewers to DM, WhatsApp or visit your page."
    },

    "Facebook": {
        "hook": "Start with a relatable problem or strong benefit.",
        "length": "30–90 seconds",
        "cta": "Ask people to comment, message or WhatsApp."
    },

    "WhatsApp Status": {
        "hook": "Keep it short because people tap quickly through Status.",
        "length": "10–30 seconds",
        "cta": "Tell viewers to WhatsApp you directly."
    },

    "YouTube Shorts": {
        "hook": "Create curiosity immediately and deliver the payoff quickly.",
        "length": "15–60 seconds",
        "cta": "Ask viewers to subscribe, comment or contact you."
    },

    "WhatsApp Message": {
        "hook": "Start with a direct benefit instead of a long introduction.",
        "length": "Short written advertisement",
        "cta": "Ask the customer to reply or WhatsApp."
    },

    "General Online Ad": {
        "hook": "Lead with the customer's problem and desired result.",
        "length": "Flexible",
        "cta": "Give the customer one clear next action."
    },
}


# ------------------------------------------------------------
# AD STYLES
# ------------------------------------------------------------

STYLE_INTROS = {
    "TikTok Girl / Gen Z":
        "Bestie, wait! 👀 You need to hear this!",

    "Professional Man":
        "If you're looking for a practical solution, listen to this.",

    "Luganda Mix":
        "Banange! Kale, wuliriza katono! 👀",

    "Friendly Seller":
        "Hey! Let me show you something that can make your life easier.",

    "Bold Salesperson":
        "Stop scrolling! This could be exactly what you've been looking for.",
}


# ------------------------------------------------------------
# GENERATOR
# ------------------------------------------------------------

def generate_ad(
    product,
    problem,
    benefit,
    price,
    platform,
    style,
    template,
    language,
    target_customer,
    location,
    contact,
    unlock_code,
):
    """
    Generate an advertising script based on the user's inputs.
    """

    product = (product or "").strip()
    problem = (problem or "").strip()
    benefit = (benefit or "").strip()
    price = (price or "").strip()
    contact = (contact or "07XXXXXXX").strip()
    location = (location or "Kampala, Uganda").strip()
    target_customer = (target_customer or "customers").strip()
    unlock_code = (unlock_code or "").strip().upper()

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not product:
        return "⚠️ Please enter the Product Name."

    if not problem:
        return "⚠️ Please enter the Problem it solves."

    if not benefit:
        return "⚠️ Please enter the Main Benefit."

    # --------------------------------------------------------
    # PRO STATUS
    # --------------------------------------------------------

    is_paid = unlock_code in UNLOCK_CODES

    # --------------------------------------------------------
    # PRICE
    # --------------------------------------------------------

    if price:
        price_line = f"💰 Price: {price}"
    else:
        price_line = "💰 Message us for today's price."

    # --------------------------------------------------------
    # STYLE
    # --------------------------------------------------------

    intro = STYLE_INTROS.get(
        style,
        "Listen to this!"
    )

    # --------------------------------------------------------
    # PLATFORM
    # --------------------------------------------------------

    guidance = PLATFORM_GUIDANCE.get(
        platform,
        PLATFORM_GUIDANCE["General Online Ad"]
    )

    # --------------------------------------------------------
    # LANGUAGE
    # --------------------------------------------------------

    language_note = ""

    if language == "Luganda Mix":
        language_note = """
Language style:
Use natural Ugandan English mixed with simple Luganda phrases.
Do not overuse Luganda. Keep the advertisement understandable.
"""

    elif language == "Ugandan English":
        language_note = """
Language style:
Use natural, simple Ugandan English.
Keep the wording conversational rather than overly corporate.
"""

    elif language == "English":
        language_note = """
Language style:
Use clear standard English.
"""

    # --------------------------------------------------------
    # CTA
    # --------------------------------------------------------

    cta = f"""
📱 WhatsApp: {contact}
📍 Location: {location}

Interested? Send us a WhatsApp message now.
"""

    # --------------------------------------------------------
    # TEMPLATE
    # --------------------------------------------------------

    if template == "POV Hook":

        script = f"""
🎬 {platform.upper()} AD

HOOK:
POV: You have been struggling with {problem.lower()}... then you discover {product}! 👀

{intro}

PROBLEM:
Let's be honest.

{problem}

SOLUTION:
That's exactly why we have {product}.

It helps you {benefit.lower()}.

WHY IT MATTERS:
Instead of continuing to struggle with {problem.lower()},
you can now have a simple solution that helps you {benefit.lower()}.

{price_line}

CTA:
If you are a {target_customer} looking for this solution,
send us a message today.

{cta}

PLATFORM TIP:
{guidance["hook"]}

Recommended length: {guidance["length"]}

{language_note}
"""

    elif template == "Problem → Solution":

        script = f"""
🎬 {platform.upper()} AD

HOOK:
Are you tired of {problem}? 😩

THE PROBLEM:
Many {target_customer} struggle with:

{problem}

THE SOLUTION:
Meet {product}.

{intro}

With {product}, you can {benefit.lower()}.

WHY BUY:
✅ Convenient
✅ Easy to understand
✅ Useful for everyday customers
✅ Available in {location}

{price_line}

CTA:
Don't keep struggling with {problem.lower()}.

Contact us today:

{cta}

PLATFORM TIP:
{guidance["hook"]}

Recommended length: {guidance["length"]}

{language_note}
"""

    elif template == "Before → After":

        script = f"""
🎬 {platform.upper()} AD

HOOK:
BEFORE vs AFTER using {product}! 😱

BEFORE:
You are dealing with:

{problem}

You are tired of searching for a solution.

AFTER:
Now imagine being able to:

{benefit}

That's where {product} comes in.

{intro}

{price_line}

CTA:
Ready to make the change?

Message us today.

{cta}

PLATFORM TIP:
{guidance["hook"]}

Recommended length: {guidance["length"]}

{language_note}
"""

    elif template == "Testimonial":

        script = f"""
🎬 {platform.upper()} AD

HOOK:
"I wish I had discovered {product} earlier!"

STORY:

I used to struggle with:

{problem}

Then I discovered {product}.

What I like most is that it helps me:

{benefit}

{intro}

If you are also dealing with {problem.lower()},
you should check it out.

{price_line}

CTA:
Want to know more?

Send us a message now.

{cta}

PLATFORM TIP:
{guidance["hook"]}

Recommended length: {guidance["length"]}

{language_note}
"""

    elif template == "Direct Sales":

        script = f"""
🎬 {platform.upper()} AD

🔥 {product} AVAILABLE NOW!

Are you struggling with:

{problem}

We have a solution.

{product} helps you:

{benefit}

{price_line}

Perfect for:
• {target_customer}
• Customers in {location}
• People looking for a convenient solution

Don't wait.

Contact us today.

{cta}

PLATFORM TIP:
{guidance["hook"]}

Recommended length: {guidance["length"]}

{language_note}
"""

    else:

        script = f"""
🎬 {platform.upper()} AD

{intro}

PRODUCT:
{product}

PROBLEM:
{problem}

BENEFIT:
{benefit}

{price_line}

CTA:
Contact us today to learn more.

{cta}

{language_note}
"""

    # --------------------------------------------------------
    # WATERMARK
    # --------------------------------------------------------

    if is_paid:
        watermark = "[Pro by Raymond]"
    else:
        watermark = "[Made with Simple Ads Creator - Free]"

    script += f"""

━━━━━━━━━━━━━━━━━━━━
{watermark}
━━━━━━━━━━━━━━━━━━━━
"""

    return script.strip()


# ------------------------------------------------------------
# EXPORT TXT
# ------------------------------------------------------------

def export_txt(script):

    if not script:
        return None

    file = tempfile.NamedTemporaryFile(
        mode="w",
        delete=False,
        suffix=".txt",
        encoding="utf-8"
    )

    file.write(script)
    file.close()

    return file.name


# ------------------------------------------------------------
# CLEAR FORM
# ------------------------------------------------------------

def clear_all():

    return (
        "",
        "",
        "",
        "",
        "TikTok",
        "TikTok Girl / Gen Z",
        "POV Hook",
        "Ugandan English",
        "",
        "Kampala, Uganda",
        "07XXXXXXX",
        "",
        "",
        None
    )


# ------------------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------------------

CSS = """

body {
    background: #f6f7f9;
}

.gradio-container {
    max-width: 1000px !important;
    margin: auto !important;
}

h1 {
    text-align: center;
}

textarea,
input {
    font-size: 16px !important;
}

button {
    min-height: 46px !important;
}

#hero {
    text-align: center;
    padding: 10px;
}

#payment {
    text-align: center;
    padding: 18px;
    border-radius: 15px;
}

#output {
    font-size: 16px !important;
}

.platform-box {
    border-radius: 15px;
}

"""


# ------------------------------------------------------------
# APP
# ------------------------------------------------------------

with gr.Blocks(
    title=APP_NAME,
    css=CSS
) as app:

    # ========================================================
    # HEADER
    # ========================================================

    gr.Markdown(
        """
# 🚀 Simple Ads Creator by Raymond

### Create ads for TikTok, Instagram, Facebook, WhatsApp & YouTube.

**Turn your product information into ready-to-use advertising copy in seconds.**

🇺🇬 Built with Ugandan sellers and small businesses in mind.
        """,
        elem_id="hero"
    )

    gr.Markdown(
        """
### 💰 FREE 3/day | UNLIMITED 20k/month

📱 MoMo: **07XXXXXXX**

💬 WhatsApp: **07XXXXXXX**
        """,
        elem_id="payment"
    )

    # ========================================================
    # PRODUCT INFORMATION
    # ========================================================

    gr.Markdown("## 🛍️ 1. Tell us about your product")

    with gr.Row():

        with gr.Column():

            product = gr.Textbox(
                label="Product Name",
                placeholder="Example: Men's Sneakers"
            )

            problem = gr.Textbox(
                label="Problem it solves",
                placeholder="Example: Uncomfortable shoes"
            )

            benefit = gr.Textbox(
                label="Main Benefit",
                placeholder="Example: Comfortable and stylish shoes"
            )

        with gr.Column():

            price = gr.Textbox(
                label="Price (Optional)",
                placeholder="Example: UGX 85,000"
            )

            target_customer = gr.Textbox(
                label="Target Customer",
                placeholder="Example: Students, men, women, parents"
            )

            location = gr.Textbox(
                label="Location",
                value="Kampala, Uganda"
            )

    # ========================================================
    # PLATFORM
    # ========================================================

    gr.Markdown("## 📱 2. Choose where you want to advertise")

    platform = gr.Dropdown(
        choices=[
            "TikTok",
            "Instagram Reels",
            "Facebook",
            "WhatsApp Status",
            "YouTube Shorts",
            "WhatsApp Message",
            "General Online Ad"
        ],
        value="TikTok",
        label="Advertising Platform"
    )

    # ========================================================
    # STYLE
    # ========================================================

    with gr.Row():

        style = gr.Dropdown(
            choices=[
                "TikTok Girl / Gen Z",
                "Professional Man",
                "Luganda Mix",
                "Friendly Seller",
                "Bold Salesperson"
            ],
            value="TikTok Girl / Gen Z",
            label="Ad Personality"
        )

        language = gr.Dropdown(
            choices=[
                "Ugandan English",
                "Luganda Mix",
                "English"
            ],
            value="Ugandan English",
            label="Language"
        )

    # ========================================================
    # TEMPLATE
    # ========================================================

    template = gr.Dropdown(
        choices=[
            "POV Hook",
            "Problem → Solution",
            "Before → After",
            "Testimonial",
            "Direct Sales"
        ],
        value="POV Hook",
        label="Advertising Template"
    )

    # ========================================================
    # CONTACT
    # ========================================================

    contact = gr.Textbox(
        label="WhatsApp / Contact Number",
        value="07XXXXXXX",
        placeholder="Example: 0700000000"
    )

    # ========================================================
    # PRO UNLOCK
    # ========================================================

    gr.Markdown("## 🔐 Pro Access")

    unlock_code = gr.Textbox(
        label="Pro Unlock Code (Optional)",
        placeholder="Enter your unlock code",
        type="password"
    )

    gr.Markdown(
        """
**Example demo codes:**

`RAYMOND2026`

`SIMPLE20K`

For the real business version, these should later be connected to a proper payment and license system.
        """
    )

    # ========================================================
    # GENERATE
    # ========================================================

    generate_btn = gr.Button(
        "🔥 CREATE MY AD",
        variant="primary",
        size="lg"
    )

    # ========================================================
    # OUTPUT
    # ========================================================

    output = gr.Textbox(
        label="🎬 Your Advertisement",
        lines=30,
        placeholder="Your generated advertisement will appear here...",
        elem_id="output"
    )

    # ========================================================
    # EXPORT
    # ========================================================

    with gr.Row():

        export_btn = gr.Button(
            "📥 Export as TXT"
        )

        clear_btn = gr.Button(
            "🗑️ Clear"
        )

    download_file = gr.File(
        label="Download your advertisement",
        visible=False
    )

    # ========================================================
    # NEXT STEPS
    # ========================================================

    gr.Markdown(
        """
## 🎥 Turn Your Script Into a Video

### Using CapCut

1. Copy your generated advertisement.
2. Open CapCut.
3. Start a new project.
4. Add your product photos/videos.
5. Add the script as text.
6. Use CapCut Text-to-Speech.
7. Add captions.
8. Add suitable background music.
9. Export your video.
10. Post it on your selected platform.

### 📱 Recommended workflow

**Simple Ads Creator → CapCut → TikTok / Instagram / Facebook / WhatsApp / YouTube**

You don't need expensive AI video tools to start.
        """
    )

    # ========================================================
    # BUSINESS SECTION
    # ========================================================

    gr.Markdown(
        """
## 🇺🇬 Built for Small Businesses

Useful for:

- JForce agents
- Online sellers
- Boutique owners
- Electronics sellers
- Beauty businesses
- Food businesses
- Kampala businesses
- Freelancers
- Small shops
- Service providers
        """
    )

    gr.Markdown(
        """
### 💰 Simple Ads Creator

**FREE 3/day | UNLIMITED 20k/month**

📱 MoMo: **07XXXXXXX**

💬 WhatsApp: **07XXXXXXX**

Replace the placeholder numbers before launching publicly.
        """,
        elem_id="payment"
    )

    # ========================================================
    # FUTURE FEATURES
    # ========================================================

    gr.Markdown(
        """
### 🔮 Future Features

Planned upgrades can include:

- AI image generation
- Product photo enhancement
- Talking product photos
- Wav2Lip integration
- Automatic video creation
- More Ugandan languages
- More advertising platforms
- Customer accounts
- Payment verification
- Analytics
        """
    )

    # ========================================================
    # BUTTON ACTIONS
    # ========================================================

    generate_btn.click(
        fn=generate_ad,
        inputs=[
            product,
            problem,
            benefit,
            price,
            platform,
            style,
            template,
            language,
            target_customer,
            location,
            contact,
            unlock_code
        ],
        outputs=output
    )

    export_btn.click(
        fn=export_txt,
        inputs=output,
        outputs=download_file
    )

    clear_btn.click(
        fn=clear_all,
        inputs=[],
        outputs=[
            product,
            problem,
            benefit,
            price,
            platform,
            style,
            template,
            language,
            target_customer,
            location,
            contact,
            unlock_code,
            output,
            download_file
        ]
    )


# ============================================================
# RUN APP
# ============================================================

if __name__ == "__main__":
    app.launch()

"""
PowerPoint Presentation Generator for Budget Overrun Early-Warning Model
Builds a professional 10-slide executive presentation deck (slides/project_deck.pptx)
using python-pptx.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

SLIDES_DIR = "slides"
DECK_PATH = os.path.join(SLIDES_DIR, "project_deck.pptx")
NAVY = RGBColor(31, 56, 100)
ACCENT = RGBColor(197, 90, 17)
DARK_GRAY = RGBColor(60, 64, 67)
LIGHT_BG = RGBColor(245, 247, 250)
WHITE = RGBColor(255, 255, 255)

def set_slide_background(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_header(slide, title_text, category_text="FP&A & CORPORATE FINANCE ANALYTICS"):
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(1.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p_cat = tf.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = ACCENT
    p_title = tf.add_paragraph()
    p_title.text = title_text
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = NAVY

def add_bullet(tf, title, body, pt_size=13):
    p = tf.add_paragraph()
    p.font.size = Pt(pt_size)
    p.space_after = Pt(10)
    r1 = p.add_run()
    r1.text = title + " "
    r1.font.bold = True
    r1.font.color.rgb = NAVY
    r2 = p.add_run()
    r2.text = body
    r2.font.color.rgb = DARK_GRAY

def build_deck():
    os.makedirs(SLIDES_DIR, exist_ok=True)
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]
    
    # Slide 1: Title
    s1 = prs.slides.add_slide(blank)
    set_slide_background(s1, NAVY)
    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(11.0), Inches(3.5))
    tf1 = tb1.text_frame
    p0 = tf1.paragraphs[0]
    p0.text = "CORPORATE FINANCE & FP&A DECISION SUPPORT"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(237, 125, 49)
    p1 = tf1.add_paragraph()
    p1.text = "Budget Overrun Early-Warning Model"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    p2 = tf1.add_paragraph()
    p2.text = "Predictive Prioritization of Mid-Year Agency Spend to Prevent Year-End Deficits"
    p2.font.size = Pt(18)
    p2.font.color.rgb = RGBColor(210, 225, 245)
    p3 = tf1.add_paragraph()
    p3.text = "Author: Bhupesh Chandra Dimri | Email: bhupesh7cd@gmail.com | October 2026"
    p3.font.size = Pt(11)
    p3.font.color.rgb = RGBColor(180, 195, 215)
    
    # Slide 2: Problem Overview
    s2 = prs.slides.add_slide(blank)
    set_slide_background(s2, LIGHT_BG)
    add_header(s2, "Executive Problem Statement: Overcoming Review Capacity Constraints")
    tb2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf2 = tb2.text_frame
    add_bullet(tf2, "The Capacity Dilemma:", "Finance and budget reviewers manage thousands of agency line items and cannot manually inspect every line at mid-year.")
    add_bullet(tf2, "The Cost of Late Discovery:", "Budget variances discovered in Q4 are unrecoverable, forcing emergency spending freezes or fiscal deficits.")
    add_bullet(tf2, "The Analytical Solution:", "A machine learning early-warning model that scores each line's risk of exceeding a 5% overrun threshold, prioritizing review where risk is concentrated.")
    add_bullet(tf2, "Proven Empirical Result:", "Reviewing the top 20% of flagged lines captures 62.1% of all overruns (a 3.1x lift over random selection), outperforming legacy burn-rate rules (35.5%).")
    
    # Slide 3: Model Benchmark
    s3 = prs.slides.add_slide(blank)
    set_slide_background(s3, LIGHT_BG)
    add_header(s3, "Model Comparison: Explainable Logistic Regression Wins")
    tb3 = s3.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf3 = tb3.text_frame
    add_bullet(tf3, "Burn-Gap Heuristic (Baseline):", "ROC-AUC 0.686 | PR-AUC 0.435 | Captures only 35.5% of overruns in top 20% volume.")
    add_bullet(tf3, "Logistic Regression (Selected Production Model):", "ROC-AUC 0.906 | PR-AUC 0.777 | Captures 62.1% of overruns in top 20% volume (3.10x lift).")
    add_bullet(tf3, "Gradient Boosting Classifier:", "ROC-AUC 0.899 | PR-AUC 0.763 | Captures 61.6% of overruns in top 20% volume.")
    add_bullet(tf3, "Controller Recommendation:", "Logistic regression matches boosting within statistical noise while offering full coefficient auditability for department heads.")
    
    # Slide 4: Drivers
    s4 = prs.slides.add_slide(blank)
    set_slide_background(s4, LIGHT_BG)
    add_header(s4, "Econometric Findings: Primary Operational Risk Drivers")
    tb4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf4 = tb4.text_frame
    add_bullet(tf4, "1. Overtime Reliance (Odds Ratio 4.36x):", "Overtime surges represent the single most acute warning signal of structural operational distress.")
    add_bullet(tf4, "2. Mid-Year Change Orders (Odds Ratio 2.95x):", "Unbudgeted scope expansion through contract change orders drives systemic overrun cascades.")
    add_bullet(tf4, "3. Prior-Year Variance Inertia (Odds Ratio 1.20x):", "Historical deficit history reflects chronic budgeting under-allocation across fiscal cycles.")
    add_bullet(tf4, "4. Burn-Rate Gap (Odds Ratio 1.32x):", "Cumulative spend exceeding the fiscal calendar pace provides empirical early warning at Month 6.")
    
    # Slide 5: Simulations & Financial ROI
    s5 = prs.slides.add_slide(blank)
    set_slide_background(s5, LIGHT_BG)
    add_header(s5, "Monte Carlo Simulation & Return on Investment")
    tb5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf5 = tb5.text_frame
    add_bullet(tf5, "5,000-Run Monte Carlo Simulation:", "Across an agency budget of $1.2B, median unmitigated overrun exposure is $30M. Early mitigation saves $3.1M annually.")
    add_bullet(tf5, "Base Case Financial Return:", "Total gross benefits of $3.2M against $110K Year-1 total cost yields Net Benefit of $3.09M (ROI > 2,800%).")
    add_bullet(tf5, "Conservative Payback Period:", "Implementation costs recovered in 1.4 months under conservative mitigation assumptions.")
    
    # Slide 6: Recommendations
    s6 = prs.slides.add_slide(blank)
    set_slide_background(s6, LIGHT_BG)
    add_header(s6, "Strategic Action Plan & Controlled Pilot Roadmap")
    tb6 = s6.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf6 = tb6.text_frame
    add_bullet(tf6, "1. Deploy 20% Capacity Review Threshold:", "Concentrate analyst reviews on the highest-risk deciles, capturing 62% of potential deficits.")
    add_bullet(tf6, "2. Enforce Change Order Governance:", "Capping mid-year change orders reduces systemic portfolio overrun probability by 38% at source.")
    add_bullet(tf6, "3. Four-Month Implementation Pilot:", "Shadow testing in Q2 checkpoint followed by full operational rollout for upcoming budget cycle.")
    add_bullet(tf6, "Contact Information:", "Bhupesh Chandra Dimri | Email: bhupesh7cd@gmail.com | Jersey City, NJ")
    
    prs.save(DECK_PATH)
    print(f"Project 1 presentation saved to {DECK_PATH}")

if __name__ == "__main__":
    build_deck()

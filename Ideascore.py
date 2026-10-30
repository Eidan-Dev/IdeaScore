from dataclasses import dataclass
from typing import List

@dataclass
class ScoreResult:
    total: int
    verdict: str
    strengths: List[str]
    risks: List[str]
    breakdown: dict

def score_idea(idea: str) -> ScoreResult:
    low = idea.lower()
    
    market = 85 if any(k in low for k in ["app","people","everyone","dev","student"]) else 70
    pain = 85 if any(k in low for k in ["automatically","organize","save","annoying","hard"]) else 65
    competition = 45 if any(k in low for k in ["photos","todo","chat","notes"]) else 70
    monetization = 88 if any(k in low for k in ["saas","pro","business","productivity"]) else 75
    feasibility = 80

    total = int(market*0.25 + pain*0.25 + feasibility*0.2 + competition*0.15 + monetization*0.15)

    breakdown = {
        "Market Size": market,
        "Pain Level": pain,
        "Feasibility": feasibility,
        "Competition": competition,
        "Monetization": monetization
    }

    strengths = []
    if market >= 80: strengths.append("Large market - Millions affected")
    if pain >= 80: strengths.append("High pain point - People will PAY")
    if monetization >= 80: strengths.append("Clear monetization (Freemium/SaaS)")
    
    risks = []
    if competition <= 50: risks.append("High competition - Need niche")
    else: risks.append("Need to validate with 10 users first")

    if total >= 80: verdict = "STRONG POTENTIAL - BUILD IT"
    elif total >= 65: verdict = "GOOD - Niche down"
    else: verdict = "RISKY - Validate first"

    return ScoreResult(total, verdict, strengths[:3], risks[:2], breakdown)
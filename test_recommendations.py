#!/usr/bin/env python
# Test script to verify recommendations
from recommendation import get_recommendations

prefs = {
    'category': 'Temple',
    'budget': '',
    'state_city': '',
    'duration': '',
    'season': '',
    'crowd': '',
    'weather': ''
}

print("\n" + "="*80)
print("TESTING RECOMMENDATION ENGINE")
print("="*80)

recs = get_recommendations(prefs, num_recommendations=15)

print(f"\n\nTotal recommendations returned: {len(recs)}")
if recs:
    print(f"\nFirst 3 recommendations:")
    for i, rec in enumerate(recs[:3], 1):
        print(f"  {i}. {rec['monument']} ({rec['city']}, {rec['state']}) - Match: {rec['match_score']}%")
else:
    print("NO RECOMMENDATIONS RETURNED")

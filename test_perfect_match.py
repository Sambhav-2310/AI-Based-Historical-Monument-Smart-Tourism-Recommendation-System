#!/usr/bin/env python
# Test perfect match logic
from app import check_match_details

# Test case: All 3 selected criteria match
rec = {
    'monument': 'Bailhongal Fort',
    'city': 'Bailhongal',
    'state': 'Karnataka',
    'category': 'Fort',
    'budget': 'Low',
    'season': 'october-march',
    'crowd_level': 'Low',
    'weather': 'Hot',
    'rating': 4.1,
    'description': 'Medieval fort',
    'match_score': 83.5
}

user_prefs = {
    'category': 'Fort',
    'budget': 'Low',
    'season': 'October',
    'state_city': '',
    'duration': '',
    'crowd': '',
    'weather': ''
}

details = check_match_details(rec, user_prefs)

print("\n" + "="*70)
print("PERFECT MATCH TEST RESULTS")
print("="*70)
print(f"\nMonument: {rec['monument']}")
print(f"User Preferences Selected: Category, Budget, Season")
print(f"\nOriginal TF-IDF Score: {details['match_percentage']}%")
print(f"Adjusted Score: {details['adjusted_match_percentage']}%")
print(f"Is Perfect Match: {details['is_perfect_match']}")
print(f"\nWhat Matches:")
for match in details['matches']:
    print(f"  ✓ {match}")
print(f"\nWhat Doesn't Match:")
if details['mismatches']:
    for mismatch in details['mismatches']:
        print(f"  ✗ {mismatch}")
else:
    print("  (None - all selected criteria match!)")
print("\n" + "="*70)

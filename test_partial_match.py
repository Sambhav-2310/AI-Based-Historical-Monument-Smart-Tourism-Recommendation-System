#!/usr/bin/env python
# Test partial match logic
from app import check_match_details

# Test case: Only 2 of 3 selected criteria match
rec = {
    'monument': 'Brihadeeswarar Temple',
    'city': 'Tanjore',
    'state': 'Tamil Nadu',
    'category': 'Temple',  # Doesn't match (user wanted Fort)
    'budget': 'Low',        # Matches!
    'season': 'october-march',  # Matches!
    'crowd_level': 'High',
    'weather': 'Hot',
    'rating': 4.5,
    'description': 'Ancient temple',
    'match_score': 72.3
}

user_prefs = {
    'category': 'Fort',     # Wants Fort, but got Temple
    'budget': 'Low',        # ✓ Matches
    'season': 'October',    # ✓ Matches
    'state_city': '',
    'duration': '',
    'crowd': '',
    'weather': ''
}

details = check_match_details(rec, user_prefs)

print("\n" + "="*70)
print("PARTIAL MATCH TEST RESULTS")
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
    print("  (None)")
print("\n" + "="*70)

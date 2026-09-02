
    # ===== Choice Offer from a new club ===== #
    if season.note < 3:
      club_offer = create_mercato_event(random_club_low(tier_club(player.club)))
      club_offer.display_event()
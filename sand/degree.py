def degree_distribution_count(g):
    return zip(*[(bin_left_side, bin_count) for bin_left_side, bin_right_side, bin_count in g.degree_distribution().bins()])

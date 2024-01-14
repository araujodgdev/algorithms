def study_schedule(permanence_period, target_time):
    present = 0

    try:
        for entrance, exit in permanence_period:
            if entrance <= target_time <= exit:
                present += 1
        return present
    except TypeError:
        return None
    raise NotImplementedError

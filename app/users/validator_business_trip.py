def valid_business_trip(user):
    if user.start_vacation is None or user.start_vacation <= user.start_business_trip <= user.finish_vacation \
            or user.start_vacation <= user.finish_business_trip <= user.finish_vacation:
        raise ValueError("командировка не может быть во время отпуска")


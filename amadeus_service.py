from amadeus import Client, ResponseError

def safety_rated_locations():
    amadeus = Client(
        client_id='REPLACE_BY_YOUR_API_KEY',
        client_secret='REPLACE_BY_YOUR_API_SECRET'
    )

    try:
        response = amadeus.safety.safety_rated_locations.by_square.get(
            north=37.810980,
            west=-122.483716,
            south=37.732007,
            east=-122.370076
        )
        print(response.data)
        return response.data
    except ResponseError as error:
        raise error

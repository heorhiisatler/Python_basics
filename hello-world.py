ip_Addr = ["192.168.5.248", "192.168.1.22", "192.168.5.247"]


def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


status = int(input("Enter status:"))
print(http_error(status))

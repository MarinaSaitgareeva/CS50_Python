def extensions():
    user_input = input("Please type file name: ").strip().lower()
    all_words = user_input.split(".")
    if len(all_words) < 2:
        file_type = "None"
    else:
        file_type = all_words[-1]

    # if file_type == "gif":
    #     print("image/gif")
    # elif file_type == "jpg" or file_type == "jpeg":
    #     print("image/jpeg")
    # elif file_type == "png":
    #     print("image/png")
    # elif file_type == "pdf":
    #     print("application/pdf")
    # elif file_type == "txt":
    #     print("text/plain")
    # elif file_type == "zip":
    #     print("application/zip")
    # else:
    #     print("application/octet-stream")

    match file_type:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


extensions()

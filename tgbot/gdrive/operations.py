def get_files(conf):
    results = conf.sacc.files().list(pageSize=10,
        fields="nextPageToken, files(id, name, mimeType)"
    ).execute()
    print(results)
    return None

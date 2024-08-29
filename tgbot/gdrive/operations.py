def get_files(conf):
    try:
        results = (
            conf.sacc.files()
            .list(pageSize=10, fields="nextPageToken, files(id, name)")
            .execute()
        )

        return results

    except Exception as e:
        print(e)
        return None

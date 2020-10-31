from moz_sql_parser import parse

def main():
    print('ABC')
    query = "select ap.app_policy_id as patch_bundle_id, rc.role_class_id as resource_group_id,rc.role_class_short_name as resource_group_name, ap.app_policy_name as patch_bundle_name, ap.created_dt as created_date,ap.modified_dt as modified_date, ap.created_by as created_by_name, ap.modified_by as modified_by_name, aprc.app_policy_id as app_policy_id_in_role_class from app_policy ap INNER JOIN app_policy_role_class aprc ON (ap.app_policy_id = aprc.app_policy_id) INNER JOIN role_classes rc ON (aprc.role_class_id = rc.role_class_id)  where ap.app_policy_type_name = 'GENERIC_PATCH_POLICY' OR ap.app_policy_type_name = 'GENERIC_DYNAMIC_PATCH_POLICY' or ap.app_policy_type_name = 'SOLARIS_PATCH_POLICY';"
    print(parse(query))


if __name__ == '__main__':
    main()
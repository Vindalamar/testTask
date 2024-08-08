import argparse


def get_config(filename: str):
    conf_dict = {}
    with open(filename) as f:
        for line in f.readlines():
            v1, v2 = line.split('=')
            conf_dict[v1] = v2.rstrip('\n')
    return conf_dict


def replacer(filename: str, conf_dict: dict):
    result = []
    with open(filename) as f:
        for line in f.readlines():
            i = 0
            line = line.rstrip('\n')
            for key in conf_dict.keys():
                if key in line:
                    count = line.count(key)
                    line = line.replace(key, conf_dict[key])
                    i += count
            result.append((i, line))

    return sorted(result, key=lambda c: c[0], reverse=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('config_filename', type=str, help='Config file path')
    parser.add_argument('sample_filename', type=str, help='Sample file path')
    args = parser.parse_args()

    d = get_config(args.config_filename)
    res = replacer(args.sample_filename, d)

    print('\n'.join([i[1] for i in res]))


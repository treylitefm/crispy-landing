import urllib2


def get_http_status_code(url):
    print url
    try:
        print 'omar'
        response = urllib2.urlopen(url)
        code = response.getcode()
        response.close()
    except urllib2.HTTPError, e:
        print 'mmomar'
        code = e.getcode()
    except urllib2.URLError, e:
        print 'ssadsmmomar'
        print e
        print 'Host',url,'is probz downed, bruh'
        code = None
    return code 



#for demo purposes
#for url in ['http://docker-dev', 'https://google.com', 'http://google.com', 'http://docker-dev:5000', 'docker-dev:5000']:
#    print get_http_status_code(url)

#if __name__ == '__main__':
#    main()

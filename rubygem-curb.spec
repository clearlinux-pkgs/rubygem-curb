#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-curb
Version  : 0.8.8
Release  : 5
URL      : https://rubygems.org/downloads/curb-0.8.8.gem
Source0  : https://rubygems.org/downloads/curb-0.8.8.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Ruby
Requires: rubygem-curb-lib
BuildRequires : curl-dev
BuildRequires : ruby
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
# Curb - Libcurl bindings for Ruby
* [rubyforge rdoc](http://curb.rubyforge.org/)
* [rubyforge project](http://rubyforge.org/projects/curb)
* [github project](http://github.com/taf2/curb/tree/master)

%package lib
Summary: lib components for the rubygem-curb package.
Group: Libraries

%description lib
lib components for the rubygem-curb package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n curb-0.8.8
gem spec %{SOURCE0} -l --ruby > rubygem-curb.gemspec

%build
gem build rubygem-curb.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
curb-0.8.8.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/curb-0.8.8 && rake --trace test TESTOPTS="-v" || : && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/curb-0.8.8.gem
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/Error/code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/Error/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/Error/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/app_connect_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/autoreferer%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/body_str-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cacert%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cacert-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cdesc-Easy.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cert%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cert-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cert_key%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cert_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/certpassword%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/certtype%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/certtype-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/clone-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/connect_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/connect_timeout%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/connect_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/content_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cookiefile%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cookiefile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cookiejar%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cookiejar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cookies%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/cookies-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/delete%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/dns_cache_timeout%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/dns_cache_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/download-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/download_speed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/downloaded_bytes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/downloaded_content_length-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/dup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/enable_cookies%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/enable_cookies%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/encoding%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/encoding-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/error-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/escape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/fetch_file_time%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/fetch_file_time%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/file_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/follow_location%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/follow_location%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ftp_commands%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ftp_commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ftp_entry_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ftp_filemethod%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ftp_filemethod-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ftp_response_timeout%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ftp_response_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/getinfo-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/head%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/head-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/header_in_body%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/header_in_body%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/header_size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/header_str-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/headers%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/headers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_auth_types%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_auth_types-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_connect_code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_delete-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_get-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_head-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_head-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_post-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_post-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_put-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/http_put-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ignore_content_length%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ignore_content_length%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/interface%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/interface-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/last_effective_url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/last_result-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/local_port%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/local_port-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/local_port_range%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/local_port_range-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/low_speed_limit%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/low_speed_limit-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/low_speed_time%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/low_speed_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/max_redirects%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/max_redirects-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/multi%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/multi-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/multipart_form_post%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/multipart_form_post%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/name_lookup_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/nosignal%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/num_connects-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/on_body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/on_complete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/on_debug-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/on_failure-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/on_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/on_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/on_progress-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/on_redirect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/on_success-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/os_errno-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/password%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/password-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/perform-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/perform-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/post-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/post_body%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/post_body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/pre_transfer_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/primary_ip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_auth_types%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_auth_types-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_port%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_port-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_tunnel%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_tunnel%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_type%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_url%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxy_url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxypwd%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/proxypwd-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/put-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/put_data%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/redirect_count-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/redirect_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/redirect_url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/request_size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/reset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/resolve_mode%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/resolve_mode-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/response_code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/setopt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ssl_verify_host%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ssl_verify_host%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ssl_verify_host-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ssl_verify_host_integer%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ssl_verify_peer%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ssl_verify_peer%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ssl_verify_result-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ssl_version%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/ssl_version-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/start_transfer_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/status-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/sym2curl-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/timeout%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/total_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/unescape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/unrestricted_auth%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/unrestricted_auth%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/upload_speed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/uploaded_bytes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/uploaded_content_length-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/url%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/url-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/use_netrc%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/use_netrc%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/use_ssl%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/use_ssl-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/useragent%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/useragent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/username%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/username-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/userpwd%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/userpwd-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/verbose%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/verbose%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Easy/version%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/AbortedByCallbackError/cdesc-AbortedByCallbackError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/AccessDeniedError/cdesc-AccessDeniedError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/Again/cdesc-Again.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/BadCallingOrderError/cdesc-BadCallingOrderError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/BadContentEncodingError/cdesc-BadContentEncodingError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/BadFunctionArgumentError/cdesc-BadFunctionArgumentError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/BadOptionSyntaxError/cdesc-BadOptionSyntaxError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/BadPasswordEnteredError/cdesc-BadPasswordEnteredError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/BadPasswordError/cdesc-BadPasswordError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/BadResumeError/cdesc-BadResumeError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CantGetHostError/cdesc-CantGetHostError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CantReconnectError/cdesc-CantReconnectError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/ConnectionFailedError/cdesc-ConnectionFailedError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/ConvFailed/cdesc-ConvFailed.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/ConvReqd/cdesc-ConvReqd.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CouldntBindError/cdesc-CouldntBindError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CouldntGetSizeError/cdesc-CouldntGetSizeError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CouldntReadError/cdesc-CouldntReadError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CouldntRetrFileError/cdesc-CouldntRetrFileError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CouldntSetASCIIError/cdesc-CouldntSetASCIIError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CouldntSetBinaryError/cdesc-CouldntSetBinaryError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CouldntStorFileError/cdesc-CouldntStorFileError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CouldntUseRestError/cdesc-CouldntUseRestError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CurlError/cdesc-CurlError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/CurlOK/cdesc-CurlOK.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/DiskFullError/cdesc-DiskFullError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/FTPError/cdesc-FTPError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/FTPQuoteError/cdesc-FTPQuoteError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/FTPSSLFailed/cdesc-FTPSSLFailed.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/FTPWriteError/cdesc-FTPWriteError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/FailedInitError/cdesc-FailedInitError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/FileError/cdesc-FileError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/FileExistsError/cdesc-FileExistsError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/FileSizeExceededError/cdesc-FileSizeExceededError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/FunctionNotFoundError/cdesc-FunctionNotFoundError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/GotNothingError/cdesc-GotNothingError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/HTTPError/cdesc-HTTPError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/HTTPFailedError/cdesc-HTTPFailedError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/HTTPPostError/cdesc-HTTPPostError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/HTTPRangeError/cdesc-HTTPRangeError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/HostResolutionError/cdesc-HostResolutionError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/IllegalOperationError/cdesc-IllegalOperationError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/InterfaceFailedError/cdesc-InterfaceFailedError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/InvalidLDAPURLError/cdesc-InvalidLDAPURLError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/InvalidPostFieldError/cdesc-InvalidPostFieldError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/LDAPError/cdesc-LDAPError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/LibraryNotFoundError/cdesc-LibraryNotFoundError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/LoginDeniedError/cdesc-LoginDeniedError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MalformedURLError/cdesc-MalformedURLError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MalformedURLUserError/cdesc-MalformedURLUserError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MalformedUserError/cdesc-MalformedUserError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MultiAddedAlready/cdesc-MultiAddedAlready.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MultiBadEasyHandle/cdesc-MultiBadEasyHandle.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MultiBadHandle/cdesc-MultiBadHandle.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MultiBadSocket/cdesc-MultiBadSocket.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MultiInitError/cdesc-MultiInitError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MultiInternalError/cdesc-MultiInternalError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MultiOutOfMemory/cdesc-MultiOutOfMemory.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MultiPerform/cdesc-MultiPerform.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/MultiUnknownOption/cdesc-MultiUnknownOption.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/NoSuchUserError/cdesc-NoSuchUserError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/NotBuiltInError/cdesc-NotBuiltInError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/NotFoundError/cdesc-NotFoundError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/ObsoleteError/cdesc-ObsoleteError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/OutOfMemoryError/cdesc-OutOfMemoryError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/PartialFileError/cdesc-PartialFileError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/PermissionError/cdesc-PermissionError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/PortFailedError/cdesc-PortFailedError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/ProxyResolutionError/cdesc-ProxyResolutionError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/ReadError/cdesc-ReadError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/RecvError/cdesc-RecvError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/RemoteFileNotFound/cdesc-RemoteFileNotFound.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSH/cdesc-SSH.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLCACertificateError/cdesc-SSLCACertificateError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLCRLBadfile/cdesc-SSLCRLBadfile.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLCaertBadFile/cdesc-SSLCaertBadFile.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLCertificateError/cdesc-SSLCertificateError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLConnectError/cdesc-SSLConnectError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLCypherError/cdesc-SSLCypherError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLEngineInitFailedError/cdesc-SSLEngineInitFailedError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLEngineNotFoundError/cdesc-SSLEngineNotFoundError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLEngineSetFailedError/cdesc-SSLEngineSetFailedError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLIssuerError/cdesc-SSLIssuerError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLPeerCertificateError/cdesc-SSLPeerCertificateError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SSLShutdownFailed/cdesc-SSLShutdownFailed.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SearchFailedError/cdesc-SearchFailedError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SendError/cdesc-SendError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/SendFailedRewind/cdesc-SendFailedRewind.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/ShareInUseError/cdesc-ShareInUseError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/TFTPError/cdesc-TFTPError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/TelnetError/cdesc-TelnetError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/TimeoutError/cdesc-TimeoutError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/TooManyRedirectsError/cdesc-TooManyRedirectsError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/UnknownIDError/cdesc-UnknownIDError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/UnknownOptionError/cdesc-UnknownOptionError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/UnsupportedProtocolError/cdesc-UnsupportedProtocolError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/Weird227FormatError/cdesc-Weird227FormatError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/WeirdPassReplyError/cdesc-WeirdPassReplyError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/WeirdPasvReplyError/cdesc-WeirdPasvReplyError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/WeirdReplyError/cdesc-WeirdReplyError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/WeirdUserReplyError/cdesc-WeirdUserReplyError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/WriteError/cdesc-WriteError.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Err/cdesc-Err.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/cancel%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/cdesc-Multi.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/default_timeout%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/default_timeout-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/download-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/get-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/http-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/idle%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/max_connects%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/perform-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/pipeline%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/post-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/put-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/remove-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Multi/requests-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/cdesc-PostField.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/content%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/content-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/content-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/content_type%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/content_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/file-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/local_file%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/local_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/name%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/remote_file%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/remote_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/set_content_proc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/PostField/to_str-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Upload/cdesc-Upload.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Upload/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Upload/offset%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Upload/offset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Upload/stream%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/Upload/stream-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/asyncdns%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/cdesc-Curl.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/conv%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/debug%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/delete-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/get-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/gssnegotiate%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/head-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/http-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/idn%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/ipv6%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/kerberos4%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/largefile%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/libz%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/ntlm%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/options-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/patch-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/post-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/postalize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/put-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/reset-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/spnego%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/ssl%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/sspi%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Curl/urlalize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Object/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Object/have_constant-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/Object/test_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/ext/page-Makefile.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/page-LICENSE.ri
/usr/lib64/ruby/gems/2.2.0/doc/curb-0.8.8/ri/page-README_markdown.ri
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/curb-0.8.8/gem.build_complete
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/curb-0.8.8/gem_make.out
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/curb-0.8.8/mkmf.log
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/README.markdown
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/doc.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/Makefile
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb.c
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb.h
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb.o
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_config.h
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_easy.c
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_easy.h
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_easy.o
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_errors.c
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_errors.h
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_errors.o
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_macros.h
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_multi.c
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_multi.h
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_multi.o
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_postfield.c
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_postfield.h
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_postfield.o
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_upload.c
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_upload.h
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_upload.o
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/extconf.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/lib/curb.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/lib/curl.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/lib/curl/easy.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/lib/curl/multi.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/alltests.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_crash_on_debug.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_crash_on_progress.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_curb_easy_blocks_ruby_threads.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_curb_easy_post_with_string_no_content_length_header.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_instance_post_differs_from_class_post.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_issue102.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_multi_segfault.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_postfields_crash.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_postfields_crash2.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bug_require_last_or_segfault.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/bugtests.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/mem_check.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/require_last_or_segfault_script.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/signals.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/tc_curl.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/tc_curl_download.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/tc_curl_easy.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/tc_curl_easy_setopt.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/tc_curl_multi.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/tc_curl_postfield.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/timeout.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/timeout_server.rb
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/tests/unittests.rb
/usr/lib64/ruby/gems/2.2.0/specifications/curb-0.8.8.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/curb-0.8.8/curb_core.so
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/ext/curb_core.so
/usr/lib64/ruby/gems/2.2.0/gems/curb-0.8.8/lib/curb_core.so

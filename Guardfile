# A sample Guardfile
# More info at https://github.com/guard/guard#readme

guard 'compass' do
  watch(/^sass\/(.*)\.s[ac]ss/)
end

# Add files and commands to this file, like the example:
#   watch(%r{file/path}) { `command(s)` }
#
guard 'shell' do
    watch(%r{stylesheets/day\.css}) {
        cmd = "foreman run rake " +
        "REDDIT_STYLESHEET_MODE=day " +
        "REDDIT_STYLESHEET_COMPILE=false " +
        "REDDIT_SUBREDDIT=crazysimreddittesttwo " +
        "deploy"
        `#{cmd}`
        }
    watch(%r{stylesheets/night\.css}) {
        cmd = "foreman run rake " +
        "REDDIT_STYLESHEET_MODE=night " +
        "REDDIT_STYLESHEET_COMPILE=false " +
        "REDDIT_SUBREDDIT=crazysimreddittest3 " +
        "deploy"
        `#{cmd}`
        }
    watch(%r{stylesheets/*\.css}) {
        cmd = "foreman run rake " +
        "REDDIT_STYLESHEET_MODE=auto " +
        "REDDIT_STYLESHEET_COMPILE=false " +
        "REDDIT_SUBREDDIT=crazysimreddittest " +
        "deploy"
        `#{cmd}`
        }
end


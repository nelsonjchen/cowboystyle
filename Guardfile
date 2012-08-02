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
        puts "Updating Day Reddit"
        cmd = "foreman run rake " +
        "REDDIT_STYLESHEET_MODE=day " +
        "REDDIT_STYLESHEET_COMPILE=false " +
        "REDDIT_SUBREDDIT=" + ENV['REDDIT_SUBREDDIT_DEV_DAY'] +
        " deploy"
        `#{cmd}`
        }
    watch(%r{stylesheets/night\.css}) {
        puts "Updating Night Reddit"
        cmd = "foreman run rake " +
        "REDDIT_STYLESHEET_MODE=night " +
        "REDDIT_STYLESHEET_COMPILE=false " +
        "REDDIT_SUBREDDIT=" + ENV['REDDIT_SUBREDDIT_DEV_NIGHT'] +
        " deploy"
        `#{cmd}`
        }
    # watch(%r{stylesheets/(day|night)\.css}) {
        # puts "Updating Temporal Reddit"
        # cmd = "foreman run rake " +
        # "REDDIT_STYLESHEET_MODE=auto " +
        # "REDDIT_STYLESHEET_COMPILE=false " +
        # "REDDIT_SUBREDDIT=" + ENV['REDDIT_SUBREDDIT_DEV_TEMPORAL'] +
        # " deploy"
        # `#{cmd}`
        # }
end


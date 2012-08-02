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
        cmd = "rake " +
        "REDDIT_STYLESHEET_MODE=day " +
        "REDDIT_STYLESHEET_COMPILE=false " +
        "deploy"
        `#{cmd}`
        }
    watch(%r{stylesheets/night\.css}) {
        cmd = "rake " +
        "REDDIT_STYLESHEET_MODE=night " +
        "REDDIT_STYLESHEET_COMPILE=false " +
        "deploy"
        `#{cmd}`
        }
end


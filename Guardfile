# A sample Guardfile
# More info at https://github.com/guard/guard#readme


guard 'compass' do
  watch(/^sass\/(.*)\.s[ac]ss/)
end

# Add files and commands to this file, like the example:
#   watch(%r{file/path}) { `command(s)` }

guard 'rake', :task => 'deploy_day', :run_on_start => false do
    watch(%r{stylesheets/day\.css})
end

guard 'rake', :task => 'deploy_night', :run_on_start => false do
    watch(%r{stylesheets/night\.css})
end

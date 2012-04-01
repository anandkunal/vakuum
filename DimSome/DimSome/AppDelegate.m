//
//  AppDelegate.m
//  DimSome
//
//  Created by Kunal Anand on 11/29/11.
//  Copyright (c) 2011 __MyCompanyName__. All rights reserved.
//

#import "AppDelegate.h"

@implementation AppDelegate

@synthesize window = _window;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    if ([[UIScreen mainScreen] brightness] == 0.0) {
        [[UIScreen mainScreen] setBrightness:1.0];
    }
    else {
        [[UIScreen mainScreen] setBrightness:0.0];
    }
    exit(0);
    
//    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
//    // Override point for customization after application launch.
//    self.window.backgroundColor = [UIColor whiteColor];
//    [self.window makeKeyAndVisible];
//    return YES;
}

@end
